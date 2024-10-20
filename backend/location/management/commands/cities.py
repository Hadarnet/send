import requests
import json

city = 'london'
_token = '0a6f7834ea89890fa426297697129e5f'

# Fetch countries data
url_countries = 'https://engine.hotellook.com/api/v2/static/countries.json'
myobj = {
    'token': _token
}

try:
    response = requests.post(url_countries, json=myobj)
    response.raise_for_status()  # Ensure we notice bad responses
    countries_data = response.json()  # Save response data
except requests.exceptions.RequestException as e:
    print("An error occurred while fetching countries data:", e)
    countries_data = {}  # Set to empty dict if error occurs

# Fetch cities data
url_locations = 'https://engine.hotellook.com/api/v2/static/locations.json'
myobj = {
    'token': _token
}

try:
    response = requests.post(url_locations, json=myobj)
    response.raise_for_status()
    results = response.json()
    print("Cities data response:", json.dumps(results, indent=4))  # Debug print
    # Check if results is a list or dict
    if isinstance(results, dict) and 'results' in results:
        cities = results['results']['locations']
    elif isinstance(results, list):
        # Handle case if `results` is a list
        print("Results is a list. Please check its structure.")
        cities = results  # or handle according to the list structure
    else:
        print("Unexpected structure of results")
        cities = []
except requests.exceptions.RequestException as e:
    print("An error occurred while fetching cities data:", e)
    cities = []

# Process cities data
query_params = []
for item in cities:
    if isinstance(item, dict) and 'location' in item and 'lat' in item['location'] and 'lon' in item['location']:
        query_param = f"{item['location']['lat']},{item['location']['lon']}"
        query_params.append(query_param)

# Search hotel
url_hotel = 'https://engine.hotellook.com/api/v2/lookup.json'
myobj = {
    'query': city,
    'lookFor': 'hotel',
    'limit': 10,
    'token': _token
}

try:
    response = requests.post(url_hotel, json=myobj)
    response.raise_for_status()
    hotels_response = response.json()
    print("Hotels response:", json.dumps(hotels_response, indent=4))
except requests.exceptions.RequestException as e:
    print("An error occurred while searching for hotels:", e)
