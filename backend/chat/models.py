from django.db import models
from user.models import User
from backend import settings
# Create your models here.

# class ChatMessage(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender")
#     reciever = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reciever")
#     message = models.CharField(max_length=100000)
#     is_read = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['date']
#         verbose_name_plural = "Message"

#     def __str__(self):
#         return f"{self.sender} - {self.reciever}"
    
# class Contact(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts')
#     contact_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacted_by')
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user', 'contact_user')

#     def __str__(self):
#         return f"{self.user} -> {self.contact_user}"
