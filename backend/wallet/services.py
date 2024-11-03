# wallet/services.py
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_connected_account(user):
    account = stripe.Account.create(
        type="express",
        country="US",  # Adjust to user's country if needed
        email=user.email,
        capabilities={"transfers": {"requested": True}},
    )
    user.stripe_account_id = account.id
    user.save()
    return account

def generate_account_link(stripe_account_id):
    account_link = stripe.AccountLink.create(
        account=stripe_account_id,
        refresh_url="https://yourdomain.com/reauth",  # Replace with your app's URL
        return_url="https://yourdomain.com/complete",  # Replace with your app's URL
        type="account_onboarding",
    )
    return account_link.url
