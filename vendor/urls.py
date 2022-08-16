from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.accounts),
    path('newvendor', views.newvendor, name='newvendor'),
    path('vendor/<str:id>', views.vendor_info),
    path('vendor/<str:id>/sell', views.vendor_info_),
    path('settings/vendor', views.vendor_settings, name='vendor_settings'),
]
