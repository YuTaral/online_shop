from django.urls import path

from online_shop.online_shop_profiles.views import profile_details

urlpatterns = [
    path('details/', profile_details, name='profile details'),

]

import online_shop.online_shop_profiles.signals
