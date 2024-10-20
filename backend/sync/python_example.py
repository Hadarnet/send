# views.py
from django.shortcuts import redirect
from django.http import HttpResponse
import requests

# הכנס את מזהי האפליקציה שלך כאן
YOUR_APP_ID = '1372070626638292'
YOUR_APP_SECRET = '6f7eb549931dfa7dbc4b41bdd20e5538'

def home(request):
    return HttpResponse('<a href="/login/">Login with Facebook</a>')

def login(request):
    # הפנה את המשתמש לאישור
    return redirect(
        f'https://www.facebook.com/v12.0/dialog/oauth?client_id={YOUR_APP_ID}&redirect_uri={request.build_absolute_uri("/callback/")}&scope=pages_show_list'
    )

def callback(request):
    code = request.GET.get('code')
    # קבל את ה-Access Token
    token_url = f'https://graph.facebook.com/v12.0/oauth/access_token?client_id={YOUR_APP_ID}&redirect_uri={request.build_absolute_uri("/callback/")}&client_secret={YOUR_APP_SECRET}&code={code}'

    response = requests.get(token_url)
    access_token = response.json().get('access_token')

    if access_token:
        pages = fetch_facebook_pages(access_token)  # כאן אתה יכול לקרוא לפונקציה שלך
        return HttpResponse(f'Access Token received! Here are your pages: {pages}')

    return HttpResponse('Failed to get access token.')

def fetch_facebook_pages(access_token):
    url = f'https://graph.facebook.com/me/accounts?access_token={access_token}'
    response = requests.get(url)

    if response.status_code == 200:
        pages_data = response.json()
        pages = []
        for page in pages_data['data']:
            pages.append(f"Page Name: {page['name']}, Page ID: {page['id']}")
        return pages
    else:
        return f"Failed to retrieve pages. Error: {response.text}"
