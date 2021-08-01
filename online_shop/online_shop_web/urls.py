from django.urls import path

from online_shop.online_shop_web.views import index

urlpatterns = [
    path('', index, name='index'),
]