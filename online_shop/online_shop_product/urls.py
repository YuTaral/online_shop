from django.urls import path

from online_shop.online_shop_product.views import landing_page, ProductCreateView

urlpatterns = [
    path('', landing_page, name='index'),
    path('item/create/', ProductCreateView.as_view(), name='create item'),
]
