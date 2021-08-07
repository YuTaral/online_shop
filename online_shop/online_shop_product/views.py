from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from online_shop.online_shop_product.models import Product


def landing_page(request):
    return render(request, 'landing_page.html')


class ProductCreateView(CreateView):
    template_name = 'items/create_item.html'
    model = Product
    fields = ('type', 'state', 'price', 'name', 'year', 'image', 'description', 'location',)
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
