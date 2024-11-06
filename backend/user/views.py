from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from rest_framework.views import APIView
from .models import OTP
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views import View
from .utils import send_otp_via_sns, generate_otp
from rest_framework.permissions import AllowAny
from wallet.models import Wallet
from django.db import transaction

User = get_user_model()
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    """
    API endpoint for user registration.
    Handles user creation, initializes the user's wallet, and provides a refresh and access token upon successful registration.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        # Validate and save the user data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = serializer.save()
            Wallet.objects.create(user=user, balance=0)
            account = user.create_connected_account()
            user.stripe_account_id = account.id
            user.save(update_fields=["stripe_account_id"])
            account_link_url = user.generate_account_link()
        # Generate tokens for the newly created user
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        # Return user data and tokens
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": {
                'refresh': str(refresh),
                'access': access,
            },
            "stripe_account_link": account_link_url,
        })

# Login API
class LoginAPI(TokenObtainPairView):
    """
    API endpoint for user login.
    Provides a refresh and access token upon successful login.
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        # Validate the login credentials
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        # Generate tokens for the authenticated user
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        # Return user data and tokens
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": {
                'refresh': str(refresh),
                'access': access,
            }
        })

# Logout API
class LogoutAPI(generics.GenericAPIView):
    """
    API endpoint for user logout.
    Blacklists the refresh token to invalidate it.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = None

    def post(self, request):
        try:
            # Extract the refresh token from the request
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Blacklist the provided refresh token
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)

# Get User API
class UserAPI(generics.RetrieveAPIView):
    """
    API endpoint for retrieving the currently authenticated user's details.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        # Return the currently authenticated user
        return self.request.user


class GenerateOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        user_id = request.data.get('user_id')  # הוסף את user_id לבקשה

        # ודא שהמשתמש קיים
        user = get_object_or_404(User, id=user_id)

        if user.is_verified:
            return Response({"error": "User is already verified!"}, status=status.HTTP_400_BAD_REQUEST)

        # בדוק אם ה-OTP כבר קיים בטבלה, אם כן, מחק אותו
        existing_otp = OTP.objects.filter(phone_number=phone_number).first()
        if existing_otp:
            existing_otp.delete()

        otp_code = generate_otp()

        # יצירת OTP עם קישור למשתמש
        OTP.objects.create(user=user, phone_number=phone_number, otp_code=otp_code)

        # שליחת ה-OTP באמצעות SMS
        send_otp_via_sns(phone_number, otp_code)
        return Response({"message": "OTP sent successfully!"}, status=status.HTTP_200_OK)

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]  # מאפשר גישה לכל אחד

    def post(self, request):
        phone_number = request.data.get('phone_number')
        entered_otp = request.data.get('otp_code')
        try:
            otp_record = OTP.objects.get(phone_number=phone_number, otp_code=entered_otp)
            user = get_object_or_404(User, id=otp_record.user_id)

            # Optionally, you can check if the OTP is expired based on created_at
            otp_record.delete()  # Delete OTP after successful verification

            # Set the is_active attribute of the user to true
            # user.is_verified = True
            # user.save()

            return Response({"message": "OTP verified successfully!"}, status=status.HTTP_200_OK)
        except OTP.DoesNotExist:
            return Response({"error": "Invalid OTP!"}, status=status.HTTP_400_BAD_REQUEST)












# class SendOTPView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

#         otp, created = OTP.objects.get_or_create(user=user)
#         otp.generate_otp()

#         send_mail(
#             'Your OTP Code',
#             f'Your OTP code is: {otp.otp_code}',
#             settings.EMAIL_HOST_USER,
#             [email]
#         )

#         return Response({"detail": "OTP sent."}, status=status.HTTP_200_OK)


# class VerifyOTPView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         otp_code = request.data.get('otp_code')

#         try:
#             user = User.objects.get(email=email)
#             otp = OTP.objects.get(user=user, otp_code=otp_code)
#         except (User.DoesNotExist, OTP.DoesNotExist):
#             return Response({"detail": "Invalid OTP or user."}, status=status.HTTP_400_BAD_REQUEST)

#         if timezone.now() - otp.created_at > timezone.timedelta(minutes=5):
#             return Response({"detail": "OTP expired."}, status=status.HTTP_400_BAD_REQUEST)

#         otp.delete()  # Optional: remove OTP after successful verification
#         return Response({"detail": "OTP verified successfully."}, status=status.HTTP_200_OK)
