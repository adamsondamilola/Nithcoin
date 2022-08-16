from django.urls import path
from . import views

urlpatterns = [
    path('transactions', views.all_transactions),
    path('transactions/<int:id>/<str:transId>/view', views.view_transactions),
]
