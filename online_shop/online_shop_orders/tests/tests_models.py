from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from online_shop.online_shop_auth.models import OnlineShopUser

from online_shop.online_shop_orders.models import Order
from online_shop.online_shop_product.models import Product


class ModelTests(TestCase):
    def test_orderer_first_name_starts_with_lowercase_expect_exception(self):
        order = Order(
            orderer_first_name='gosho',
            orderer_last_name='Georgiev',
            address_street='Vasil Levski 21',
            address_city='Plovdiv',
            address_country='Bulgaria',
        )

        with self.assertRaises(ValidationError) as context:
            order.full_clean()
            order.save()

        self.assertIsNotNone(context.exception)

    def test_orderer_last_name_starts_with_lowercase_expect_exception(self):
        order = Order(
            orderer_first_name='Gosho',
            orderer_last_name='georgiev',
            address_street='Vasil Levski 21',
            address_city='Plovdiv',
            address_country='Bulgaria',
        )

        with self.assertRaises(ValidationError) as context:
            order.full_clean()
            order.save()

        self.assertIsNotNone(context.exception)

    def test_orderer_first_name_and_last_name_starts_with_uppercase_expect_to_create_it(self):
        test_user = OnlineShopUser.objects.create(email='gosho@abv.bg', password='qwe123')
        test_user.full_clean()
        test_user.save()

        test_product = Product(
            type='Car',
            name='Toyota',
            price='10000',
            state='Brand new',
            year=2020,
            image='https://t1-cms-3.images.toyota-europe.com/toyotaone/ieen/Header_Cover_tcm-3044-1887120.jpg',
            description='Electrical Toyota',
            location='Japan',
            quantity=2,
            user=test_user,
        )
        test_product.full_clean()
        test_product.save()

        order = Order(
            orderer_first_name='Gosho',
            orderer_last_name='Georgiev',
            address_street='Vasil Levski 21',
            address_city='Plovdiv',
            address_country='Bulgaria',
            time=datetime.now(),
            user=test_user,
            product=test_product,
            postal_code='2500',

        )

        order.full_clean()
        order.save()

