# serializers.py
from rest_framework import serializers
from .models import Message, SocialMediaMessage, Notification, Call, Email, SMS, Chat, VideoCall, ChatMessage, Contact
from user.models import User
from user.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class SocialMediaMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaMessage
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class VideoCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCall
        fields = '__all__'

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']  

class ContactSimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'pic', 'banner', 'bio', 'phone', 'facebook', 'twitter', 'instagram', 'linkedin', 'website']
class MessageSerializer(serializers.ModelSerializer):
    reciever_profile = SimpleUserSerializer(read_only=True, source='reciever')
    sender_profile = SimpleUserSerializer(read_only=True, source='sender')

    class Meta:
        model = ChatMessage
        fields = ['id', 'reciever_profile', 'sender_profile', 'message', 'is_read', 'date']
        read_only_fields = ['sender', 'is_read']  # Make 'sender' read-only

    def __init__(self, *args, **kwargs):
        super(MessageSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')

        # Only include 'sender' and 'reciever' fields during POST requests
        if request and request.method == 'POST':
            self.fields['sender'] = serializers.PrimaryKeyRelatedField(read_only=True)
            self.fields['reciever'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        else:
            self.Meta.depth = 2

    def create(self, validated_data):
        # Automatically assign the sender to the logged-in user
        request = self.context.get('request')
        validated_data['sender'] = request.user
        return super().create(validated_data)

class SaveContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = Contact
        fields = ['email']

    def validate_email(self, value):
        # Check if a user with this email exists
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def create(self, validated_data):
        # Create a contact using the validated email and associate the user
        user = User.objects.get(email=validated_data['email'])
        request = self.context.get('request')
        contact = Contact.objects.create(user=request.user, contact_user=user)
        contact.save()
        return contact

class RetrieveContactSerializer(serializers.ModelSerializer):
    contact_user_profile = ContactSimpleUserSerializer(read_only=True, source='contact_user')

    class Meta:
        model = Contact
        fields = ['id', 'user', 'contact_user_profile']
        read_only_fields = ['id', 'user', 'contact_user_profile']
