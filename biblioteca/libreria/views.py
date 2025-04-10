from django.shortcuts import render
from libreria.models import Autor
from rest_framework.views import APIView
from libreria.serializers import AutoresSerializer
from rest_framework.response import Response

# Create your views here.
class AutoresListAV(APIView):
    
    def get(self, request):
        autor = Autor.objects.all()
        serializer = AutoresSerializer(autor, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AutoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    
    