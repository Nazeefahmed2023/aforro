
from django.urls import path
from .views import product_list, product_detail

# Endpoints for product listing and detail
urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
]
