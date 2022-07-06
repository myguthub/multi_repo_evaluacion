from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from .serializers import ItemSerializer
from api import serializers

@api_view(['GET'])    # api decorator
def getData(request):
    items = User.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data) 

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid(): # data validation
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid(): # data validation
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid(): # data validation
        serializer.delete()
    return Response(serializer.data)