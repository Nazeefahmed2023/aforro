
from django.contrib import admin
from .models import Category, Product

# Register models for Django admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'price', 'category')
	list_filter = ('category',)
	search_fields = ('title',)

# TODO: Add custom admin filters if needed
