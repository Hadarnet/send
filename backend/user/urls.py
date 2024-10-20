# Djando Imports
from django.urls import path, include

# Third party imports
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

# Local imports
from . import views

# Api URLs
urlpatterns = [

    # Endpoint for user registration
    path('register/', views.RegisterAPI.as_view(), name='register'),

    # Endpoint for obtaining a new JWT token pair (access and refresh tokens) upon login
    path('login/', views.LoginAPI.as_view(), name='token_obtain_pair'),

    # Endpoint for refreshing the access token using a valid refresh token
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoint for logging out and blacklisting the JWT token
    path('logout/', views.LogoutAPI.as_view(), name='token_blacklist'),

    # Endpoint for retrieving user details
    path('', views.UserAPI.as_view(), name='user_detail'),

    # Endpoint for updating user details
    path('send-otp/', views.GenerateOTPView.as_view(), name='send_otp'),

    # Endpoint for verifying OTP
    path('verify-otp/', views.VerifyOTPView.as_view(), name='verify_otp'),

]
