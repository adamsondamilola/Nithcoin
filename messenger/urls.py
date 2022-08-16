from django.urls import path
from . import views

urlpatterns = [
    path('messenger/<int:id>/contact', views.messenger, name='messenger'),
    path('messenger/inbox', views.inbox, name='inbox'),
    path('messenger/sent', views.sent, name='sent'),
    path('messenger/requests', views.requests, name='requests'),
]
