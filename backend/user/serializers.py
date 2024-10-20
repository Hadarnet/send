from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from business.serializers import BusinessSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from user.models import OTP

User = get_user_model()

# API View for listing businesses related to a user
class UserBusinessListView(generics.GenericAPIView):
    """
    API endpoint for retrieving the list of businesses associated with a specific user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id, *args, **kwargs):
        try:
            # Retrieve the user by ID
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            # Return 404 if the user does not exist
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve businesses associated with the user
        businesses = user.get_businesses()

        # Serialize the list of businesses
        serializer = BusinessSerializer(businesses, many=True)

        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user details including associated businesses.
    """
    businesses = BusinessSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'banner', 'pic', 'birthday', 
            'phone', 'facebook', 'twitter', 'instagram', 'linkedin', 'website', 
            'bio', 'is_verified', 'is_active', 'is_staff', 'businesses'
        )

    def get_businesses(self, obj):
        """
        Retrieve and serialize businesses related to the user.
        """
        return BusinessSerializer(obj.get_businesses(), many=True).data

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration, handles password creation.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
    
    def create(self, validated_data):
        """
        Create a new user with the provided email and password.
        Password is hashed using the create_user method.
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# Serializer for user login
class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login credentials validation.
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """
        Validate login credentials and authenticate the user.
        """
        email = data.get('email')
        password = data.get('password')

        if email and password:
            # Authenticate the user
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if user:
                if user.is_active:
                    return user
                raise serializers.ValidationError("User account is not active.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['otp_code']


