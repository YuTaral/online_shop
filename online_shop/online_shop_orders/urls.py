from django.urls import path
from online_shop.online_shop_orders.views import product_ordered_message, OrderProduct, \
    view_order_requests

urlpatterns = [
    path('product/order/<int:pk>', OrderProduct.as_view(), name='order product'),
    path('product-ordered-message/', product_ordered_message, name='product ordered message'),
    path('order-requests/', view_order_requests, name='order requests'),
]
