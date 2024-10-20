# Django Imports
from django.contrib import admin
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Admin view for the Message model.
    """
    # Display these fields in the list view.
    list_display = (
        'id',                  # Unique identifier for the message
        'email',               # Email associated with the message
        'phone',               # Phone number associated with the message
        'subject',             # Subject of the message
        'message',             # Content of the message
        'created_at',          # Timestamp when the record was created
        'modified_at',         # Timestamp when the record was last modified
        'business',            # Associated business
        'user'                 # Associated user
    )
    
    # Fields to be included in the search functionality.
    search_fields = (
        'email',               # Search by email
        'phone',               # Search by phone number
        'subject',             # Search by subject
        'message'              # Search by message content
    )
    
    # Fields to filter by in the list view.
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
        'business',            # Filter by associated business
        'user'                 # Filter by associated user
    )

@admin.register(models.SocialMediaMessage)
class SocialMediaMessageAdmin(admin.ModelAdmin):
    """
    Admin view for the SocialMediaMessage model.
    """
    # Display these fields in the list view.
    list_display = (
        'id',                  # Unique identifier for the social media message
        'platform',            # Platform of the message
        'message_id',          # Message ID
        'text',                # Content of the message
        'created_at',          # Timestamp when the record was created
        'updated_at',          # Timestamp when the record was last modified
        'status',              # Status of the message
        'business'             # Associated business
    )
    
    # Fields to be included in the search functionality.
    search_fields = (
        'message_id',          # Search by message ID
        'text'                 # Search by message content
    )
    
    # Fields to filter by in the list view.
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'updated_at',          # Filter by modification timestamp
        'platform',            # Filter by platform
        'status',              # Filter by status
        'business'             # Filter by associated business
    )

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Admin view for the Notification model.
    """
    # Display these fields in the list view.
    list_display = (
        'id',                  # Unique identifier for the notification
        'message',             # Content of the notification
        'created_at',          # Timestamp when the record was created
        'modified_at',         # Timestamp when the record was last modified
        'business',            # Associated business
        'user'                 # Associated user
    )
    
    # Fields to be included in the search functionality.
    search_fields = (
        'message',             # Search by notification content
    )
    
    # Fields to filter by in the list view.
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
        'business',            # Filter by associated business
        'user'                 # Filter by associated user
    )

@admin.register(models.Call)
class CallAdmin(admin.ModelAdmin):
    """
    Admin view for the Call model.
    """
    # Display these fields in the list view.
    list_display = (
        'id',                  # Unique identifier for the call
        'phone',               # Phone number associated with the call
        'duration',            # Duration of the call
        'created_at',          # Timestamp when the record was created
        'modified_at',         # Timestamp when the record was last modified
        'business',            # Associated business
        'user'                 # Associated user
    )
    
    # Fields to be included in the search functionality.
    search_fields = (
        'phone',               # Search by phone number
        'duration'             # Search by call duration
    )
    
    # Fields to filter by in the list view.
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
        'business',            # Filter by associated business
        'user'                 # Filter by associated user
    )

@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    """
    Admin view for the Email model.
    """
    # Display these fields in the list view.
    list_display = (
        'id',                  # Unique identifier for the email
        'email',               # Email address
        'subject',             # Subject of the email
        'message',             # Content of the email
        'created_at',          # Timestamp when the record was created
        'modified_at',         # Timestamp when the record was last modified
        'business',            # Associated business
        'user'                 # Associated user
    )
    
    # Fields to be included in the search functionality.
    search_fields = (
        'email',               # Search by email address
        'subject',             # Search by subject
        'message'              # Search by email content
    )
    
    # Fields to filter by in the list view.
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
        'business',            # Filter by associated business
        'user'                 # Filter by associated user
    )

@admin.register(models.SMS)
class SMSAdmin(admin.ModelAdmin):
    """
    Admin view for the SMS model.
    """
    # Display these fields in the list view.
    list_display = (
        'id',                  # Unique identifier for the SMS
        'phone',               # Phone number associated with the SMS
        'message',             # Content of the SMS
        'created_at',          # Timestamp when the record was created
        'modified_at',         # Timestamp when the record was last modified
        'business',            # Associated business
        'user'                 # Associated user
    )
    
    # Fields to be included in the search functionality.
    search_fields = (
        'phone',               # Search by phone number
        'message'              # Search by SMS content
    )
    
    # Fields to filter by in the list view.
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
        'business',            # Filter by associated business
        'user'                 # Filter by associated user
    )

@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    """
    Admin view for the Chat model.
    """
    # Display these fields in the list view.
    list_display = (
        'id',                  # Unique identifier for the chat
        'message',             # Content of the chat message
        'created_at',          # Timestamp when the record was created
        'modified_at',         # Timestamp when the record was last modified
        'business',            # Associated business
        'user'                 # Associated user
    )
    
    # Fields to be included in the search functionality.
    search_fields = (
        'message',             # Search by chat content
    )
    
    # Fields to filter by in the list view.
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
        'business',            # Filter by associated business
        'user'                 # Filter by associated user
    )

@admin.register(models.VideoCall)
class VideoCallAdmin(admin.ModelAdmin):
    """
    Admin view for the VideoCall model.
    """
    # Display these fields in the list view.
    list_display = (
        'id',                  # Unique identifier for the video call
        'duration',            # Duration of the video call
        'created_at',          # Timestamp when the record was created
        'modified_at',         # Timestamp when the record was last modified
        'business',            # Associated business
        'user'                 # Associated user
    )
    
    # Fields to be included in the search functionality.
    search_fields = (
        'duration',            # Search by duration of the video call
    )
    
    # Fields to filter by in the list view.
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
        'business',            # Filter by associated business
        'user'                 # Filter by associated user
    )
