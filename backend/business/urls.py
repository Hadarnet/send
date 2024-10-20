from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for searching businesses by name and category
    path('search/', views.BusinessSearchView.as_view(), name='business-search'),

    # URL pattern for retrieving, updating, or deleting a specific business by its UUID
    path('filter/', views.BusinessFilterView.as_view(), name='business-filter'),

    # URL pattern for listing all businesses
    path('list/', views.BusinessListView.as_view(), name='business-list'),

    # URL pattern for creating a new business or listing all businesses
    path('create/', views.BusinessCreateView.as_view(), name='business-list-create'),

    # URL pattern for retrieving a specific business by its UUID
    path('<uuid:business_id>/', views.BusinessDetailView.as_view(), name='business-detail'),

    # URL pattern for listing businesses associated with a specific user
    path('my/<int:user_id>/', views.UserBusinessListView.as_view(), name='user-business-list'),

    # URL pattern for retrieving, updating, or deleting a specific business by its UUID
    path('mybusiness/<uuid:business_id>/', views.MyBusinessListView.as_view(), name='my-business'),

]
