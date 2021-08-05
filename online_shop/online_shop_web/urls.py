from django.urls import path

from online_shop.online_shop_web.views import landing_page

urlpatterns = [
    path('', landing_page, name='index'),
]