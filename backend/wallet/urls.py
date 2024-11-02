from django.urls import path
from . import views


urlpatterns = [
    path('deposit/', views.DepositView.as_view(), name='deposit'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
]