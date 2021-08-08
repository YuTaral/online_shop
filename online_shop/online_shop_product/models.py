from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Product(models.Model):
    TYPE_CHOICE_FASHION = 'Fashion'
    TYPE_CHOICE_COMPUTER = 'Computer'
    TYPE_CHOICE_PHONE = 'Phone'
    TYPE_CHOICE_CAR = 'Car'
    TYPE_CHOICE_ACCOMMODATION = 'Accommodation'
    TYPE_CHOICE_ACCESSORY = 'Accessory'

    TYPE_CHOICES = (
        (TYPE_CHOICE_FASHION, 'Fashion'),
        (TYPE_CHOICE_COMPUTER, 'Computer'),
        (TYPE_CHOICE_PHONE, 'Phone'),
        (TYPE_CHOICE_CAR, 'Car'),
        (TYPE_CHOICE_ACCOMMODATION, 'Accommodation'),
        (TYPE_CHOICE_ACCESSORY, 'Accessory'),
    )

    STATE_CHOICE_USED = 'Used'
    STATE_CHOICE_BRAND_NEW = 'Brand new'

    STATE_CHOICES = (
        (STATE_CHOICE_USED, 'Used'),
        (STATE_CHOICE_BRAND_NEW, 'Brand new'),
    )

    type = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
    )

    name = models.CharField(
        max_length=15,

    )

    price = models.FloatField()

    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
    )

    year = models.PositiveIntegerField()

    image = models.ImageField(
        upload_to='products',
    )

    description = models.TextField(
        max_length=250,
    )

    location = models.CharField(
        max_length=30,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
