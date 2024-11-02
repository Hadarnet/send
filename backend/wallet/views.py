from django.shortcuts import render
from backend import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from .models import Wallet, Transaction
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY
# print(stripe.api_key)
# Create your views here.


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
        
class StripeWebhookView(View):
    def post(self, request):
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except ValueError:
            return JsonResponse({"error": "Invalid payload"}, status=400)
        except stripe.error.SignatureVerificationError:
            return JsonResponse({"error": "Invalid signature"}, status=400)

        # Process successful checkout session completion
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            user_id = session['metadata']['user_id']
            amount = int(session['metadata']['amount'])

            # Update wallet balance for the user
            Wallet.objects.filter(user_id=user_id).update(balance=F('balance') + amount)

        return JsonResponse({"status": "success"}, status=200)