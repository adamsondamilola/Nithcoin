from django.contrib import admin
from django.urls import path, include

#to handle file uploads
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('dashboard.urls')),
    path('', include('auth_user.urls')),
    path('', include('wallet.urls')),
    path('', include('vendor.urls')),
    path('', include('account.urls')),
    path('', include('users.urls')),
    path('', include('messenger.urls')),
    path('', include('transactions.urls')),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
