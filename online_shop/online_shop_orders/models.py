from django.core.validators import MinLengthValidator
from django.db import models

from core.validators import first_letter_uppercase_validator
from online_shop.online_shop_auth.admin import UserModel
from online_shop.online_shop_product.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    orderer_first_name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), first_letter_uppercase_validator]

    )

    orderer_last_name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), first_letter_uppercase_validator]

    )

    address_street = models.CharField(
        max_length=20,
    )

    address_city = models.CharField(
        max_length=20,
    )

    address_country = models.CharField(
        max_length=20,
    )

    postal_code = models.CharField(
        max_length=20,
    )

    time = models.DateTimeField()
