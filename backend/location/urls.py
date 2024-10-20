from django.urls import path
from . import views

urlpatterns = [

    # Endpoint for listing and creating continents
    path('continents/', views.ContinentListCreateAPIView.as_view(), name='continent-list-create'),

    # Endpoint for retrieving, updating, or deleting a specific continent
    path('continents/<int:pk>/', views.ContinentDetailAPIView.as_view(), name='continent-detail'),

    # Endpoint for listing and creating countries
    path('countries/', views.CountryListCreateAPIView.as_view(), name='country-list-create'),

    # Endpoint for retrieving, updating, or deleting a specific country
    path('countries/<int:pk>/', views.CountryDetailAPIView.as_view(), name='country-detail'),

    # Endpoint for listing and creating cities
    path('cities/', views.CityListCreateAPIView.as_view(), name='city-list-create'),

    # Endpoint for retrieving, updating, or deleting a specific city
    path('cities/<int:pk>/', views.CityDetailAPIView.as_view(), name='city-detail'),

    # Endpoint for listing and creating streets
    path('streets/', views.StreetListCreateAPIView.as_view(), name='street-list-create'),

    # Endpoint for retrieving, updating, or deleting a specific street
    path('streets/<int:pk>/', views.StreetDetailAPIView.as_view(), name='street-detail'),

]





