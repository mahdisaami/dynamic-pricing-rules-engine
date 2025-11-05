from django.contrib import admin

from cart.models import CartItem, Cart


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price')

    def total_price(self, obj):
        return obj.total_price()

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_items', 'subtotal')

    def get_items(self, obj):
        return ", ".join([str(item) for item in obj.items.all()])
    get_items.short_description = "Items"