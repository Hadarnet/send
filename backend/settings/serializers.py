# Django REST Framework Imports
from rest_framework import serializers
from . import models

class UserSettingsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the UserSettings model.
    Provides serialization and deserialization for UserSettings instances.
    """
    
    class Meta:
        model = models.UserSettings  # The model to be serialized
        fields = '__all__'
      
