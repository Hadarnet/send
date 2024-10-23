from django.db import models
from backend import settings

class Message(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return self.message

class SocialMediaMessage(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('tiktok', 'TikTok'),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    message_id = models.CharField(max_length=255, unique=True)
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='social_media_messages')
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.platform} - {self.message_id}'

class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='notifications')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='notifications')

    def __str__(self):
        return self.message

class Call(models.Model):
    phone = models.CharField(max_length=15)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='calls')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='calls')

    def __str__(self):
        return self.phone

class Email(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='emails')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='emails')

    def __str__(self):
        return self.email

class SMS(models.Model):
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='sms')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='sms')

    def __str__(self):
        return self.phone

class Chat(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='chats')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='chats')

    def __str__(self):
        return self.message

class VideoCall(models.Model):
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='video_calls')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='video_calls')

    def __str__(self):
        return str(self.duration)

class ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="sender")
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="reciever")
    message = models.CharField(max_length=100000)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Message"

    def __str__(self):
        return f"{self.sender} - {self.reciever}"
    
class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts')
    contact_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacted_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'contact_user')

    def __str__(self):
        return f"{self.user} -> {self.contact_user}"
