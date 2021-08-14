from django.test import TestCase, Client
from django.urls import reverse


class OrderTests(TestCase):
    def test_order_product(self):
        client = Client()
        self.client.get(reverse('product ordered message'))
        self.client.post(reverse('order product', args=(1,)))
        self.assertTemplateUsed('product_order.html')

    def test_product_ordered_message(self):
        client = Client()
        self.client.get(reverse('product ordered message'))
        self.assertTemplateUsed('product_ordered_message.html')

    def test_view_order_requests(self):
        client = Client()
        self.client.get(reverse('order requests'))
        self.assertTemplateUsed('order_requests.html')