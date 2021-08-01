from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('online_shop.online_shop_auth.urls')),
    path('', include('online_shop.online_shop_web.urls')),
    path('', include('online_shop.online_shop_profiles.urls')),
]
