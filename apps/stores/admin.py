
from django.contrib import admin
from .models import Store

# Register Store model for Django admin
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'location')
	search_fields = ('name', 'location')

# TODO: Add custom admin actions if needed
