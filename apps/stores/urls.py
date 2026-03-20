
from django.urls import path
from .views import store_list
from apps.orders.views import list_orders, list_inventory

# Endpoints for store listing, orders, and inventory
urlpatterns = [
    path('', store_list, name='store_list'),
    path('<int:store_id>/orders/', list_orders, name='list_orders'),
    path('<int:store_id>/inventory/', list_inventory, name='list_inventory'),
]
# Note: Add more store endpoints here if needed.
