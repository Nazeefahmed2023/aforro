
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Store
from .serializers import StoreSerializer

@api_view(['GET'])
def store_list(request):
    """
    List all stores, including id, name, and location.
    """
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)
