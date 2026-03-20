"""
Main URL configuration for the Aforro backend project.

Routes all API endpoints and the demo frontend.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/products/', include('apps.products.urls')),
    path('api/stores/', include('apps.stores.urls')),
    path('api/orders/', include('apps.orders.urls')),
    path('api/search/', include('apps.search.urls')),

    # Demo HTML frontend
    path('', TemplateView.as_view(template_name='aforro_demo.html'), name='aforro-demo'),
]
