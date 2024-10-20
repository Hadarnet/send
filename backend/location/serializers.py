from rest_framework import serializers
from .models import Continent, Country, City, Street

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['name']  # Include only 'name'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'longitude', 'latitude']  # Exclude 'continent'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'longitude', 'latitude']  # Exclude 'country'

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['name', 'longitude', 'latitude']  # Exclude 'city'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Remove 'city' from the representation
        representation.pop('city', None)
        return representation
