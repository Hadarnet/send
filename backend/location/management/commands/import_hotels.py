import os
import django

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

import requests
import json
import uuid
import csv
from location.models import Country, City, Street
from business.models import Business
from ecommerce.models import Product, Inventory, PriceProduct
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count


# Find duplicate businesses by name
duplicates = Business.objects.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)

# Function to save hotel data from the API


def save_hotels_from_csv(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            try:
                hotel_id = str(row.get('id', 'unknown_id'))
                uuid_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, hotel_id))
                hotel_name = row.get('name', 'Unknown Hotel')

                # Fetch or create the country, city, and street
                country_name = row.get('country_name', '')
                country, _ = Country.objects.get_or_create(name=country_name)

                city_name = row.get('location_name', '')
                city, _ = City.objects.get_or_create(name=city_name, country=country)

                # Latitude and longitude
                latitude = float(row.get('latitude', 0)) if row.get('latitude') else 0
                longitude = float(row.get('longitude', 0)) if row.get('longitude') else 0

                # Rating
                rating = float(row.get('stars', 0)) if row.get('stars') else 0

                # Check if the Business with the same ID or name already exists
                business, created = Business.objects.update_or_create(
                    id=uuid_id,  # Use the UUID here for unique identification
                    defaults={
                        'name': hotel_name,
                        'website': '',
                        'description': '',
                        'active': True,
                        'email': '',
                        'phone': '',
                        'country': country,
                        'city': city,                 
                        'street': None,  # Set to None if not needed
                        'zip': '',
                        'logo': None,
                        'banner': None,
                        'verified': False,
                        'verified_on': None,
                        'verified_by': None,
                        'verified_status': '',
                        'verified_file': None,
                        'latitude': latitude,  # Save latitude
                        'longitude': longitude,  # Save longitude
                        'rating': rating,  # Save rating
                    }
                )

                if not created:
                    print(f"Updated business from CSV: {business.name} (ID: {business.id})")
                else:
                    print(f"Saved new business from CSV: {business.name} (ID: {business.id})")

            except KeyError as e:
                print(f"Missing key in CSV data: {e}")

            except ObjectDoesNotExist as e:
                print(f"Object does not exist: {e}")

    print("Hotels imported successfully from CSV")

# Run both functions

save_hotels_from_csv('en.csv')