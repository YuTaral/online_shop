from django.urls import path

from online_shop.online_shop_product.views import ProductDetailsView, ProductDeleteView, ProductEditView, \
    own_products_list

from online_shop.online_shop_product.views import landing_page, ProductCreateView, ProductListView

urlpatterns = [
    path('', landing_page, name='index'),
    path('product/create/', ProductCreateView.as_view(), name='product create'),
    path('products/list/', ProductListView.as_view(), name='products list'),
    path('product/details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product delete'),
    path('product/edit/<int:pk>', ProductEditView.as_view(), name='product edit'),
    path('own/products/', own_products_list, name='own products'),
]
