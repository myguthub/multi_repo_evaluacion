from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .serializers import ItemSerializer

@api_view(['GET'])    # api decorator
def getData(request):
    items = User.objects.all()
    serializer = ItemSerializer(items, many=True)
    
    return Response(serializer.data) 



