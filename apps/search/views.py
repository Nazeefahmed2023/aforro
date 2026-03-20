

# Views for search endpoints.
# Provides product search and autocomplete functionality.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from .rate_limit import rate_limit
from apps.orders.models import Inventory


@api_view(['GET'])
@rate_limit
def suggest(request):
	"""
	Autocomplete endpoint for product titles.
	- Requires at least 3 characters.
	- Prefix matches appear before general matches.
	- Returns up to 10 titles.
	- Rate limited per IP.
	"""
	q = request.GET.get('q', '')
	if len(q) < 3:
		return Response([])
	# Prefix matches first, then other matches
	prefix_matches = Product.objects.filter(title__istartswith=q).values_list('title', flat=True)
	other_matches = Product.objects.filter(~Q(title__istartswith=q), title__icontains=q).values_list('title', flat=True)
	titles = list(prefix_matches) + list(other_matches)
	return Response(titles[:10])


@api_view(['GET'])
def search_products(request):
	"""
	Product search endpoint.
	- Supports keyword search on title, description, and category name.
	- Optional filters: category, price range, store, in_stock.
	- Sorting: price, newest, relevance.
	- Pagination metadata included.
	- If store_id is provided, includes inventory quantity for that store.
	"""
	q = request.GET.get('q', '')
	category = request.GET.get('category')
	price_min = request.GET.get('price_min')
	price_max = request.GET.get('price_max')
	store_id = request.GET.get('store_id')
	in_stock = request.GET.get('in_stock')
	sort = request.GET.get('sort', 'relevance')
	page = int(request.GET.get('page', 1))
	page_size = int(request.GET.get('page_size', 20))

	products = Product.objects.all()
	# Keyword search
	if q:
		products = products.filter(
			Q(title__icontains=q) |
			Q(description__icontains=q) |
			Q(category__name__icontains=q)
		)
	# Filter by category
	if category:
		products = products.filter(category_id=category)
	# Filter by price range
	if price_min:
		products = products.filter(price__gte=price_min)
	if price_max:
		products = products.filter(price__lte=price_max)
	# Filter by store and/or in_stock
	if store_id and in_stock:
		products = products.filter(inventories__store_id=store_id, inventories__quantity__gt=0)
	elif store_id:
		products = products.filter(inventories__store_id=store_id)
	elif in_stock:
		products = products.filter(inventories__quantity__gt=0)

	# Sorting
	if sort == 'price':
		products = products.order_by('price')
	elif sort == 'newest':
		products = products.order_by('-id')
	# else: relevance (default)

	total = products.count()
	start = (page - 1) * page_size
	end = start + page_size
	results = []
	for p in products[start:end]:
		item = ProductSerializer(p).data
		# If store_id is provided, include inventory quantity for that store
		if store_id:
			inv = Inventory.objects.filter(store_id=store_id, product=p).first()
			item['inventory_quantity'] = inv.quantity if inv else 0
		results.append(item)
	return Response({
		'count': total,
		'page': page,
		'page_size': page_size,
		'results': results
	})
