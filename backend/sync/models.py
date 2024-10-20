from django.db import models


# Create your models here.

class SocialMediaMessage(models.Model):
    messages = models.TextField()
    platform = models.CharField(max_length=200)