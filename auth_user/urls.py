from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('reset/', views.reset, name='reset'),
    path('reset/<str:unique>', views.reset_pass, name='reset_pass'),
    path('reset/confirm/<str:unique>', views.confirm_reset),
    path('invite/<str:invitee>', views.invite),
    path('logout/', views.logUserOut, name='logout'),
]
