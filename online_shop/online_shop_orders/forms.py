from django.forms import models

from core.mixins import BootstrapFormMixin
from online_shop.online_shop_orders.models import Order
from online_shop.online_shop_product.models import Product


class OrderForm(BootstrapFormMixin, models.ModelForm):
    class Meta:
        model = Order
        fields = ('orderer_first_name', 'orderer_last_name', 'address_street', 'address_city', 'address_country', 'postal_code')

