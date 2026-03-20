
from django.urls import path
from .views import create_order

# Endpoints for order creation (add more as needed)
urlpatterns = [
    path('', create_order, name='create_order'),
]
