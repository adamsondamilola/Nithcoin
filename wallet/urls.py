from django.urls import path
from . import views

urlpatterns = [
    path('wallet', views.wallet),
    path('buy', views.buy, name='buy'),
    path('buy/search/<str:countryname>', views.search_seller),
    path('sell/search/<str:countryname>', views.search_buyer),
    path('sell', views.sell),
    path('swap', views.swap),
    path('send', views.send),
    path('send/<str:amt>/<str:acc>/<str:wal>', views.confirm_send),
    path('receive', views.receive),
    path('withdraw', views.withdraw),
]
