from django.shortcuts import render
from backend import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.db.models import F
from .models import Wallet, Transaction
from user.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .serializers import TransactionSerializer
import json
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY
# print(stripe.api_key)
# Create your views here.

class BalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            wallet = Wallet.objects.get(user=user)
            balance = wallet.balance
            return Response({"balance": balance}, status=200)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=404)

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_wallet = Wallet.objects.get(user=self.request.user)
        return Transaction.objects.filter(wallet=user_wallet).order_by('-timestamp')
class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class DepositView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000/"
        
        try:
            # Stripe API call to create a product and price
            product = stripe.Product.create(name='Wallet Deposit')
            amount_in_cents = int(request.data["amount"] * 100) 

            price = stripe.Price.create(
                product=product.id,
                unit_amount=amount_in_cents,
                currency='usd',
            )

            # Stripe Checkout session
            checkout_session = stripe.checkout.Session.create(
                customer_email=request.user.email,
                line_items=[
                    {
                        'price': price.id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + 'wallet/deposit/success/',
                cancel_url=YOUR_DOMAIN + 'wallet/deposit/cancel/',
            )
            # print("addasd")
            return Response({"url": checkout_session.url}, status=200)
            # return redirect(checkout_session.url, code=303)

        except Exception as e:
           
            print(f"Error creating Stripe session: {str(e)}")
            return Response({"error": str(e)}, status=400)

def handle_checkout_session(session):
    try:
        # Retrieve the amount and user identifier
        amount = session['amount_total'] / 100 
        user_email = session['customer_email']  

        user = User.objects.get(email=user_email)

        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(user=user)
            wallet.balance = F("balance") + amount
            wallet.save(update_fields=["balance"])
            Transaction.objects.create(
                wallet=wallet,
                type=Transaction.DEPOSIT,
                amount=amount
            )

        print("Balance updated successfully for user:", user.email)
    except User.DoesNotExist:
        print("User with email {} does not exist.".format(user_email))
    except Wallet.DoesNotExist:
        print("Wallet does not exist for user:", user.email)

@csrf_exempt
def my_webhook_view(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
    )
  except ValueError as e:
    # Invalid payload
    print('Error parsing payload: {}'.format(str(e)))
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    print('Error verifying webhook signature: {}'.format(str(e)))
    return HttpResponse(status=400)

  try:
    event = stripe.Event.construct_from(
      json.loads(payload), stripe.api_key
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)

  # Handle the event
  if event.type == 'checkout.session.completed':
    session = event.data.object
    # Then define and call a method to handle the successful payment intent.
    handle_checkout_session(session)

  else:
    print('Unhandled event type {}'.format(event.type))

  return HttpResponse(status=200)


class TransferView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        sender = request.user
        recipient_email = request.data.get("recipient_email")
        amount = request.data.get("amount")
        
        # Validate the amount and recipient
        if amount is None or amount <= 0:
            return Response({"error": "Invalid transfer amount."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            recipient_wallet = Wallet.objects.select_for_update().get(user__email=recipient_email)
            sender_wallet = Wallet.objects.select_for_update().get(user=sender)
            
            # Ensure sender has enough balance
            if sender_wallet.balance < amount:
                return Response({"error": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)

            # Transfer within an atomic transaction
            with transaction.atomic():
                sender_wallet.balance -= amount
                recipient_wallet.balance += amount
                sender_wallet.save(update_fields=["balance"])
                recipient_wallet.save(update_fields=["balance"])
                Transaction.objects.create(
                wallet=sender_wallet,
                type=Transaction.TRANSFER,
                amount=-amount  # Negative amount for sender's record
                )
                Transaction.objects.create(
                    wallet=recipient_wallet,
                    type=Transaction.TRANSFER,
                    amount=amount  # Positive amount for recipient's record
                )

            return Response({"message": "Transfer successful."}, status=status.HTTP_200_OK)

        except Wallet.DoesNotExist:
            return Response({"error": "Recipient not found."}, status=status.HTTP_404_NOT_FOUND)