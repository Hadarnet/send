from rest_framework import serializers
from . import models
from location.serializers import StreetSerializer, CitySerializer, CountrySerializer

class BusinessSerializer(serializers.ModelSerializer):
    """
    Serializer for the Business model, including related location data.
    """
    # Nested serializers to represent related location data
    street = StreetSerializer()  # Serialize the related Street object
    city = CitySerializer()  # Serialize the related City object
    country = CountrySerializer()  # Serialize the related Country object
    
    class Meta:
        model = models.Business
        fields = '__all__'  # Include all fields from the Business model

class MyBusinessSerializer(serializers.ModelSerializer):
    """
    Serializer for the MyBusiness model.
    """
    class Meta:
        model = models.MyBusiness
        fields = '__all__'  # Include all fields from the MyBusiness model
