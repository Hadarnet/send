from django.urls import path
from . import views
from .views import chatgpt_response
from .python_example import home, login, callback

urlpatterns = [
    path('facebook/login/', views.FacebookLoginView.as_view(), name='facebook_login'),
    path('facebook/callback/', views.FacebookCallbackView.as_view(), name='facebook_callback'),
    path('facebook/pages/', views.FacebookPagesView.as_view(), name='facebook_pages'),
    path('facebook/groups/', views.FacebookGroupView.as_view(), name='facebook_groups'),
    path('facebook/page-messages/', views.FacebookPageMessagesView.as_view(), name='facebook_page_messages'),
    path('facebook/group-messages/', views.FacebookGroupMessagesView.as_view(), name='facebook_group_messages'),
    path('search-photos/', views.search_photos, name='search_photos'),
    path('chatgpt/', chatgpt_response, name='chatgpt_response'),

    # python_example.py
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('callback/', callback, name='callback'),
]
