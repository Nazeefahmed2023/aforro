
from django.urls import path
from .views import suggest, search_products

# URL patterns for search-related endpoints.
urlpatterns = [
    path('suggest/', suggest, name='suggest'),  # Autocomplete for product titles
    path('products/', search_products, name='search_products'),  # Product search
]
# Add more search endpoints here as needed.
