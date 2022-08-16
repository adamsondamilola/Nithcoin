from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings),
    path('referral/', views.referral),
    path('credit_card/', views.credit_card),
]
