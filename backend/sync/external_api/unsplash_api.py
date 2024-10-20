# external_apis/unsplash_client.py

import requests

class UnsplashClient:
    def __init__(self, access_key):
        self.base_url = "https://api.unsplash.com"
        self.access_key = access_key

    def search_photos(self, query, per_page=10):
        url = f"{self.base_url}/search/photos"
        params = {
            "query": query,
            "per_page": per_page,
            "client_id": self.access_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
