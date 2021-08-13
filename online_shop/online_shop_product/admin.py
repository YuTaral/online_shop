from django.contrib import admin

from online_shop.online_shop_product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'price', 'state')
    sortable_by = 'type'


admin.site.register(Product, ProductAdmin)
