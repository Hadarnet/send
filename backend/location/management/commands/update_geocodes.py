import requests
from django.core.management.base import BaseCommand
from location.models import Country, City, Street, Continent

class Command(BaseCommand):
    help = 'Update latitude and longitude for all geographic models'

    def handle(self, *args, **options):
        api_key = 'AIzaSyA6XA_OzhL1KXqLz4wovjCgAbW5eYHBC_U'
        geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'

        # Update continents
        for continent in Continent.objects.all():
            self._update_location(continent.name, geocode_url, api_key, model=Continent)

        # Update countries
        for country in Country.objects.all():
            self._update_location(country.name, geocode_url, api_key, model=Country)

        # Update cities
        for city in City.objects.all():
            self._update_location(city.name, geocode_url, api_key, model=City)

        # Update streets
        for street in Street.objects.all():
            self._update_location(street.name, geocode_url, api_key, model=Street)

    def _update_location(self, name, geocode_url, api_key, model):
        params = {
            'address': name,
            'key': api_key
        }
        response = requests.get(geocode_url, params=params)
        print(response.json())  # להדפיס את התגובה כדי לבדוק בעיות
        data = response.json()

        if data['status'] == 'OK' and data['results']:
            result = data['results'][0]
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            model.objects.filter(name=name).update(latitude=lat, longitude=lng)
            self.stdout.write(self.style.SUCCESS(f'Updated {model.__name__.lower()} {name}: {lat}, {lng}'))
        else:
            self.stdout.write(self.style.WARNING(f'No results found for {name} or error occurred'))
