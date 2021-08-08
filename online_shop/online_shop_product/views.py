from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from core.mixins import LoginRequiredMixin
from online_shop.online_shop_product.forms import ProductEditForm
from online_shop.online_shop_product.models import Product


def landing_page(request):
    return render(request, 'landing_page.html')


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'products/product_create.html'
    model = Product
    fields = ('type', 'state', 'price', 'name', 'year', 'image', 'description', 'location',)
    success_url = reverse_lazy('products list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    model = Product


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context['product']

        is_owner = product.user == self.request.user
        context['is_owner'] = is_owner

        return context


class ProductEditView(LoginRequiredMixin, UpdateView):
    template_name = 'products/product_edit.html'
    form_class = ProductEditForm
    model = Product
    success_url = reverse_lazy('own products')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    success_url = reverse_lazy('own products')


def own_products_list(request):
    products = Product.objects.all()
    own_products = []
    for p in products:
        if p.user_id == request.user.id:
            own_products.append(p)
    context = {
        'products': own_products,
    }

    return render(request, 'products/own_products_list.html', context)

