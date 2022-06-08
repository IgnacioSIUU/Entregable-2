from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Arte
from .serializers import ArteSerializer
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_arte(request):
    """
    Lista todos las artes
    """
    if request.method == 'GET':
        arte = Arte.objects.all()
        serializer = ArteSerializer(arte, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
