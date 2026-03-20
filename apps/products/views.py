
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
	"""
	List all products in the database.
	"""
	products = Product.objects.all()
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
	"""
	Retrieve a single product by its primary key (ID).
	Returns 404 if not found.
	"""
	try:
		product = Product.objects.get(pk=pk)
	except Product.DoesNotExist:
		return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
	serializer = ProductSerializer(product)
	return Response(serializer.data)
