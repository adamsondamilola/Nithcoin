from django.urls import path
from . import views

urlpatterns = [
    path('account/numbers', views.numbers),
    path('account/numbers/<str:num>', views.view_number),
]
