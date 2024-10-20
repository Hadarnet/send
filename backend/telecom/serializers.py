# serializers.py
from rest_framework import serializers
from .models import Message, SocialMediaMessage, Notification, Call, Email, SMS, Chat, VideoCall

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
