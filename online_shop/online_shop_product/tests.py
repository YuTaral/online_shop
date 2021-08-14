from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

from online_shop.online_shop_auth.models import OnlineShopUser
from online_shop.online_shop_product.models import Product


class ProductTests(TestCase):
    def test_landing_page(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed('landing_page.html')

    def test_product_create_view(self):
        client = Client()
        response = client.get(reverse('product create'))
        self.assertTemplateUsed('product_create.html')

    def test_product_list_view(self):
        client = Client()
        response = client.get(reverse('products list'))
        self.assertTemplateUsed('products_list.html')

    def test_product_details_view(self):
        client = Client()
        self.client.post(reverse('product details', args=(1,)))
        self.assertTemplateUsed('product_details.html')

    def test_product_edit_view(self):
        client = Client()
        self.client.post(reverse('product edit', args=(1,)))
        self.assertTemplateUsed('product_edit.html')

    def test_product_delete_view(self):
        client = Client()
        self.client.post(reverse('product delete', args=(1,)))
        self.assertTemplateUsed('product_delete.html')

    def test_own_products_list(self):
        client = Client()
        response = client.get(reverse('own products'))
        self.assertTemplateUsed('own_products_list.html')

    def test_search_products(self):
        client = Client()
        response = client.get(reverse('search products'))
        self.assertTemplateUsed('product_search.html')
