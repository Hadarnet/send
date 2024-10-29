from django.shortcuts import render
from backend import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from .models import Wallet, Transaction
from django.http import JsonResponse
from django.views import View
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

class DepositView(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        try:
            # Create a Stripe Checkout Session
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                mode="payment",
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": "Wallet Deposit",
                            },
                            "unit_amount": int(amount) * 100,  # Stripe works with cents
                        },
                        "quantity": 1,
                    }
                ],
                metadata={"user_id": request.user.id},
                success_url="https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url="https://yourdomain.com/cancel",
            )

            # Return the session ID to the frontend
            return Response({"session_id": session.id}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
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