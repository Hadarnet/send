from rest_framework import serializers
# from chat.models import ChatMessage, Contact
from user.serializers import UserSerializer
from user.models import User

# class SimpleUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'first_name', 'last_name']  # only essential fields


# class MessageSerializer(serializers.ModelSerializer):
#     reciever_profile = SimpleUserSerializer(read_only=True, source='reciever')
#     sender_profile = SimpleUserSerializer(read_only=True, source='sender')

#     class Meta:
#         model = ChatMessage
#         fields = ['id', 'reciever_profile', 'sender_profile', 'message', 'is_read', 'date']
#         read_only_fields = ['sender', 'is_read']  # Make 'sender' read-only

#     def __init__(self, *args, **kwargs):
#         super(MessageSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')

#         # Only include 'sender' and 'reciever' fields during POST requests
#         if request and request.method == 'POST':
#             self.fields['sender'] = serializers.PrimaryKeyRelatedField(read_only=True)
#             self.fields['reciever'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#         else:
            
#             self.Meta.depth = 2

#     def create(self, validated_data):
#         # Automatically assign the sender to the logged-in user
#         request = self.context.get('request')
#         validated_data['sender'] = request.user
#         return super().create(validated_data)

# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = ('id', 'user', 'contact_user', 'created_at')
#         read_only_fields = ('created_at',)