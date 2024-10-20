# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message, SocialMediaMessage, Notification, Call, Email, SMS, Chat, VideoCall
from .serializers import MessageSerializer, SocialMediaMessageSerializer, NotificationSerializer, CallSerializer, EmailSerializer, SMSSerializer, ChatSerializer, VideoCallSerializer

class MessageAPIView(APIView):
    def get(self, request, business_id):
        messages = Message.objects.filter(business_id=business_id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class SocialMediaMessageAPIView(APIView):
    def get(self, request, business_id):
        social_media_messages = SocialMediaMessage.objects.filter(business_id=business_id)
        serializer = SocialMediaMessageSerializer(social_media_messages, many=True)
        return Response(serializer.data)

class NotificationAPIView(APIView):
    def get(self, request, business_id):
        notifications = Notification.objects.filter(business_id=business_id)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class CallAPIView(APIView):
    def get(self, request, business_id):
        calls = Call.objects.filter(business_id=business_id)
        serializer = CallSerializer(calls, many=True)
        return Response(serializer.data)

class EmailAPIView(APIView):
    def get(self, request, business_id):
        emails = Email.objects.filter(business_id=business_id)
        serializer = EmailSerializer(emails, many=True)
        return Response(serializer.data)

class SMSAPIView(APIView):
    def get(self, request, business_id):
        sms = SMS.objects.filter(business_id=business_id)
        serializer = SMSSerializer(sms, many=True)
        return Response(serializer.data)

class ChatAPIView(APIView):
    def get(self, request, business_id):
        chats = Chat.objects.filter(business_id=business_id)
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

class VideoCallAPIView(APIView):
    def get(self, request, business_id):
        video_calls = VideoCall.objects.filter(business_id=business_id)
        serializer = VideoCallSerializer(video_calls, many=True)
        return Response(serializer.data)
