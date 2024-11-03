from django.urls import path
from . import views


urlpatterns = [
    path('balance/', views.BalanceView.as_view(), name='balance'),
    path('deposit/', views.DepositView.as_view(), name='deposit'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('webhook/', views.my_webhook_view, name='stripe-webhook'),
    path('transfer/', views.TransferView.as_view(), name='wallet_transfer'),
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
]