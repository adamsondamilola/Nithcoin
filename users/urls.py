from django.urls import path
from . import views

urlpatterns = [
    path('settings/user', views.user_settings),
]
