# services.py
import requests
from django.utils.dateparse import parse_datetime
from ..models import SocialMediaMessage

class SocialMediaService:
    def __init__(self, access_token):
        self.access_token = access_token

    def fetch_facebook_messages(self, business_id):
        url = f'https://graph.facebook.com/v14.0/{business_id}/messages'
        params = {
            'access_token': self.access_token,
            'fields': 'id,message,created_time,status'
        }
        response = requests.get(url, params=params)
        return response.json().get('data', [])

    def fetch_instagram_messages(self, business_id):
        url = f'https://graph.instagram.com/v14.0/{business_id}/messages'
        params = {
            'access_token': self.access_token,
            'fields': 'id,text,created_time,status'
        }
        response = requests.get(url, params=params)
        return response.json().get('data', [])

    def fetch_tiktok_messages(self, business_id):
        url = f'https://open.tiktokapis.com/v1/messages'
        params = {
            'access_token': self.access_token,
            'business_id': business_id,
            'fields': 'id,text,created_time,status'
        }
        response = requests.get(url, params=params)
        return response.json().get('data', [])

    def sync_messages(self, platform, business_id):
        fetch_method = getattr(self, f'fetch_{platform}_messages', None)
        if not fetch_method:
            raise ValueError(f'Unsupported platform: {platform}')

        messages = fetch_method(business_id)
        for message in messages:
            SocialMediaMessage.objects.update_or_create(
                message_id=message['id'],
                defaults={
                    'platform': platform,
                    'business': business_id,
                    'text': message.get('message', message.get('text', '')),
                    'created_at': parse_datetime(message['created_time']),
                    'status': message.get('status', 'unknown')
                }
            )
