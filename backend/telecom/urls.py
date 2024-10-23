from django.urls import path
from . import views

urlpatterns = [
    path('messages/<uuid:business_id>/', views.MessageAPIView.as_view(), name='message-list'),
    path('social-media-messages/<uuid:business_id>/', views.SocialMediaMessageAPIView.as_view(), name='social-media-message-list'),
    path('notifications/<uuid:business_id>/', views.NotificationAPIView.as_view(), name='notification-list'),
    path('calls/<uuid:business_id>/', views.CallAPIView.as_view(), name='call-list'),
    path('emails/<uuid:business_id>/', views.EmailAPIView.as_view(), name='email-list'),
    path('smms/<uuid:business_id>/', views.SMSAPIView.as_view(), name='sms-list'),
    path('chats/<uuid:business_id>/', views.ChatAPIView.as_view(), name='chat-list'),
    path('video-calls/<uuid:business_id>/', views.VideoCallAPIView.as_view(), name='video-call-list'),

    path("my-messages/", views.MyInbox.as_view()),
    path("get-messages/<reciever_id>/", views.GetMessages.as_view()),
    path("send-messages/", views.SendMessages.as_view()),

    #Endpoints For Contacts
    path('contacts/', views.GetAllContactsView.as_view(), name='get-contacts'),
    path('contacts/<int:id>/', views.ContactDetailView.as_view(), name='get-contact'),
    path('contacts/save/', views.SaveContactView.as_view(), name='save-contact'),
]





