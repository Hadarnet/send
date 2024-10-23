# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message, SocialMediaMessage, Notification, Call, Email, SMS, Chat, VideoCall, ChatMessage, Contact
from .serializers import MessageSerializer, SocialMediaMessageSerializer, NotificationSerializer, CallSerializer, EmailSerializer, SMSSerializer, ChatSerializer, VideoCallSerializer, SaveContactSerializer, RetrieveContactSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics, permissions
from django.db.models import Q
from user.models import User
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

class MyInbox(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = self.request.user.id  

        messages = ChatMessage.objects.filter(
            Q(sender_id=user_id) | Q(reciever_id=user_id)
        ).order_by('-date') #Descending

        return messages


class GetMessages(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        reciever_id = self.kwargs['reciever_id']
        sender_id = self.request.user.id  # Get the logged-in user as sender

        messages = ChatMessage.objects.filter(
            Q(sender_id=sender_id, reciever_id=reciever_id) |
            Q(sender_id=reciever_id, reciever_id=sender_id)
        ).order_by('date')  # Show messages in ascending order

        # Set is_read to True for all these messages only when the receiver calls the get-messages/ API
        messages.filter(reciever_id=self.request.user.id).update(is_read=True)
        return messages

    
class SendMessages(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save()


#Views for Contacts

# Save a contact
class SaveContactView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SaveContactSerializer  

    def post(self, request):
        serializer = self.get_serializer(data=request.data) 
        if serializer.is_valid():
            # Check if the contact already exists
            user = request.user
            email = serializer.validated_data.get('email')
            contact_user = User.objects.get(email=email)
            if Contact.objects.filter(user=user, contact_user=contact_user).exists():
                return Response({"error": "Contact already exists."}, status=status.HTTP_400_BAD_REQUEST)
            contact = serializer.save() 
            return Response({"message": "Contact saved successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllContactsView(generics.ListAPIView):
    """
    API endpoint for retrieving all contacts of the authenticated user.
    """
    serializer_class = RetrieveContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return all contacts for the authenticated user
        return Contact.objects.filter(user=self.request.user)

class ContactDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            contact = Contact.objects.get(id=id)  # Retrieve contact by ID
            serializer = RetrieveContactSerializer(contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found."}, status=status.HTTP_404_NOT_FOUND)