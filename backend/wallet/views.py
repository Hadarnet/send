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
from django.utils import timezone
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
            product = stripe.Product.create(name='Wallet Deposit', images=["https://static.vecteezy.com/system/resources/previews/007/853/706/large_2x/wallet-illustration-on-a-background-premium-quality-symbols-icons-for-concept-and-graphic-design-vector.jpg"])
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
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)

    # Handle different event types
    if event.type == 'checkout.session.completed':
        session = event.data.object
        handle_checkout_session(session)

    elif event.type == 'payout.paid':
        payout = event.data.object
        # Retrieve metadata from payout
        user_id = payout.metadata.get("user_id")
        wallet_id = payout.metadata.get("wallet_id")
        amount = float(payout.metadata.get("amount", 0))

        try:
            # Fetch the user's wallet
            wallet = Wallet.objects.get(id=wallet_id)

            # Deduct balance and log the transaction
            with transaction.atomic():
                wallet.balance = F("balance") - amount
                wallet.save(update_fields=["balance"])

                # Create the transaction record
                Transaction.objects.create(
                    wallet=wallet,
                    type=Transaction.WITHDRAWAL,
                    amount=amount,
                    timestamp=timezone.now(),
                )
            return HttpResponse(status=200)

        except Wallet.DoesNotExist:
            # Wallet does not exist; log error or handle accordingly
            return HttpResponse(status=400)

    else:
        # Log unhandled events
        print(f'Unhandled event type {event.type}')

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
        
class WithdrawView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Parse request data
        amount = float(request.data.get("amount", 0))
        user = request.user
        user_wallet = user.wallet
        stripe_account_id = user.stripe_account_id

        # Check if user has a connected account
        if not stripe_account_id:
            account = user.create_connected_account()
            user.stripe_account_id = account.id
            user.save(update_fields=["stripe_account_id"])
            account_link_url = user.generate_account_link()
            return Response({"account_link_url": account_link_url}, status=status.HTTP_200_OK)
        
        # Ensure sufficient funds
        if user_wallet.balance < amount:
            return Response({"error": "Insufficient funds."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Create a Stripe payout request (without updating the wallet balance yet)
            payout = stripe.Transfer.create(
                amount=int(amount * 100),  # Convert to cents
                currency="usd",
                destination=stripe_account_id,
                metadata={"user_id": user.id, "wallet_id": user_wallet.id, "amount": amount},
            )

            return Response({"message": "Payout initiated successfully"}, status=status.HTTP_200_OK)
        
        except stripe.error.InvalidRequestError as e:
            # Check for the specific error related to missing transfer capabilities
            if "capabilities enabled" in str(e):
                account_link_url = user.generate_account_link()
                return Response({"account_link_url": account_link_url}, status=status.HTTP_200_OK)
            else:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)