from django.shortcuts import render
from django.db.models import Q, Subquery, OuterRef
from rest_framework import generics
# from chat.models import ChatMessage
from user.models import User
# from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated

# # Create your views here.

# class MyInbox(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = MessageSerializer

#     def get_queryset(self):
#         user_id = self.request.user.id  

#         messages = ChatMessage.objects.filter(
#             Q(sender_id=user_id) | Q(reciever_id=user_id)
#         ).order_by('-date') #Descending

#         return messages


# class GetMessages(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = MessageSerializer

#     def get_queryset(self):
#         reciever_id = self.kwargs['reciever_id']
#         sender_id = self.request.user.id  # Get the logged-in user as sender

#         messages = ChatMessage.objects.filter(
#             Q(sender_id=sender_id, reciever_id=reciever_id) |
#             Q(sender_id=reciever_id, reciever_id=sender_id)
#         ).order_by('date')  # Show messages in ascending order

#         # Set is_read to True for all these messages
#         messages.update(is_read=True)

#         return messages

    
# class SendMessages(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = MessageSerializer

#     def perform_create(self, serializer):
#         serializer.save()  # The sender will be set to the logged-in user in the serializer