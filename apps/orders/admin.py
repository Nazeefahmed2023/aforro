
from django.contrib import admin
from .models import Inventory, Order, OrderItem

# Register models for Django admin
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
	list_display = ('store', 'product', 'quantity')
	search_fields = ('store__name', 'product__title')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'store', 'status', 'created_at')
	list_filter = ('status', 'store')
	date_hierarchy = 'created_at'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('order', 'product', 'quantity_requested')
	search_fields = ('order__id', 'product__title')

# TODO: Add custom admin actions if needed
