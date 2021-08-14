from django.contrib import admin

from online_shop.online_shop_orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'orderer_first_name', 'orderer_last_name')
    sortable_by = 'time'


admin.site.register(Order, OrderAdmin)
