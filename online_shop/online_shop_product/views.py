from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from core.mixins import LoginRequiredMixin
from online_shop.online_shop_product.forms import ProductEditForm, ProductForm
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


def search_products(request):
    matched_products = []

    if request.method == 'GET':
        form = ProductForm()

    else:
        type = request.POST.get('category')
        state = request.POST.get('state')
        starting_price = request.POST.get('starting_price')
        final_price = request.POST.get('final_price')

        products = Product.objects.all()

        for p in products:
            if p.type == type and p.state == state and (float(starting_price) <= p.price <= float(final_price)):
                matched_products.append(p)

        context = {
            'products': matched_products,
        }

        # return render(request, 'products/products_found.html', context)

    return render(request, 'products/product_search.html')


@login_required
def order_product(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_num')
        street = request.POST.get('street')
        st_number = request.POST.get('st_number')
        city = request.POST.get('city')
        country = request.POST.get('country')
        code = request.POST.get('postal_code')

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'street': street,
            'st_number': st_number,
            'city': city,
            'country': country,
            'code': code,
        }

    else:
        return render(request, 'products/product_order.html')

    return render(request, 'products/product_ordered_message.html', context)
