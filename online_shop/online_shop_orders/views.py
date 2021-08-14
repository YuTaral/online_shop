from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from online_shop.online_shop_orders.forms import OrderForm
from online_shop.online_shop_orders.models import Order
from online_shop.online_shop_product.models import Product


@login_required()
def product_ordered_message(request):
    return render(request, 'products/../../templates/orders/product_ordered_message.html')


class OrderProduct(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('product ordered message')
    template_name = 'products/../../templates/orders/product_order.html'


    def form_valid(self, form):
        order = form.save(commit=False)
        product = Product.objects.get(pk=self.kwargs['pk'])

        order.user = self.request.user
        order.product_id = product.id
        order.time = datetime.now()

        return super().form_valid(form)


@login_required()
def view_order_requests(request):
    orders = Order.objects.all()
    products = Product.objects.all()

    ordered_products = []
    my_order_requests = []

    for order in orders:
        for product in products:
            if order.product_id == product.id:
                product = Product.objects.get(pk=order.product_id)
                if product.user_id == request.user.id:
                    ordered_products.append(product)
                    my_order_requests.append(order)

    context = {
        'ordered_products': ordered_products,
        'my_order_requests': my_order_requests,
    }

    a = 5

    return render(request, 'orders/order_requests.html', context)
