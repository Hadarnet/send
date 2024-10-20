from django.urls import path
from . import views

urlpatterns = [
    # Endpoint to get or update details of a specific user by primary key (pk)
    path('users/<int:pk>/', views.UserSettingsByUserView.as_view(), name='user-detail'),

]
