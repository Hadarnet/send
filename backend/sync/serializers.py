# serializers.py
from rest_framework import serializers

class FacebookPageSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    access_token = serializers.CharField(allow_blank=True, required=False)

class FacebookPageMessageSerializer(serializers.Serializer):
    id = serializers.CharField()
    message = serializers.CharField(allow_blank=True, required=False)
    created_time = serializers.DateTimeField()

class FacebookGroupSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField(allow_blank=True, required=False)
    privacy = serializers.CharField(allow_blank=True, required=False)