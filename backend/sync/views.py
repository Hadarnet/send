from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View
import facebook
from .service import UnsplashClient
import openai


# הגדר את מפתח ה-API שלך
openai.api_key = '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'

def chatgpt_response(request):
    prompt = request.GET.get('prompt', '')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return JsonResponse({'response': response.choices[0].message['content'].strip()})
    except openai.error.AuthenticationError:
        return JsonResponse({'error': 'Authentication error. Please check your API key.'}, status=401)


def search_photos(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({'error': 'Query parameter is required'}, status=400)

    client = UnsplashClient(access_key=settings.UNSPLASH_ACCESS_KEY)
    results = client.search_photos(query)

    return JsonResponse(results)


# Facebook Login View
class FacebookLoginView(View):
    def get(self, request, *args, **kwargs):
        oauth_dialog_url = (
            f"https://www.facebook.com/v14.0/dialog/oauth?"
            f"client_id={settings.FACEBOOK_APP_ID}&redirect_uri={settings.FACEBOOK_REDIRECT_URI}&"
            f"scope=public_profile,pages_manage_posts,pages_read_engagement,groups_access_member_info"
        )
        return redirect(oauth_dialog_url)

# Facebook Callback View
class FacebookCallbackView(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        graph = facebook.GraphAPI(version='v14.0')
        token_info = graph.get_access_token_from_code(
            code=code,
            app_id=settings.FACEBOOK_APP_ID,
            app_secret=settings.FACEBOOK_APP_SECRET,
            redirect_uri=settings.FACEBOOK_REDIRECT_URI,
        )
        request.session['oauth_token'] = token_info['access_token']
        return redirect('facebook_pages')

# Facebook Pages View
class FacebookPagesView(View):
    def get(self, request, *args, **kwargs):
        token = request.session.get('oauth_token')
        if not token:
            return JsonResponse({'error': 'No access token found'}, status=401)

        graph = facebook.GraphAPI(access_token=token, version='v14.0')
        pages = graph.get_object('/me/accounts')
        return JsonResponse(pages)

# Facebook Groups View
class FacebookGroupView(View):
    def get(self, request, *args, **kwargs):
        token = request.session.get('oauth_token')
        if not token:
            return JsonResponse({'error': 'No access token found'}, status=401)

        graph = facebook.GraphAPI(access_token=token, version='v14.0')
        groups = graph.get_object('/me/groups')
        return JsonResponse(groups)

# Facebook Page Messages View
class FacebookPageMessagesView(View):
    def get(self, request, *args, **kwargs):
        token = request.session.get('oauth_token')
        if not token:
            return JsonResponse({'error': 'No access token found'}, status=401)

        graph = facebook.GraphAPI(access_token=token, version='v14.0')
        messages = graph.get_object('/me/conversations')
        return JsonResponse(messages)

# Facebook Group Messages View
class FacebookGroupMessagesView(View):
    def get(self, request, *args, **kwargs):
        token = request.session.get('oauth_token')
        if not token:
            return JsonResponse({'error': 'No access token found'}, status=401)

        graph = facebook.GraphAPI(access_token=token, version='v14.0')
        group_messages = graph.get_object('/me/groups')
        return JsonResponse(group_messages)
