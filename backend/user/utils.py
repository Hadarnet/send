import boto3
from django.conf import settings
import random

def send_otp_via_sns(phone_number, otp_code):
    sns = boto3.client(
        'sns',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )
    message = f"Your OTP code is: {otp_code}"
    sns.publish(PhoneNumber=phone_number, Message=message)

def generate_otp():
    return str(random.randint(100000, 999999))  # Generates a 6-digit OTP