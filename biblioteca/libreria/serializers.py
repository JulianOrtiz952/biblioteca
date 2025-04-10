from rest_framework import serializers
from libreria.models import Autor, Libro, Resena

class AutoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Autor
        fields = '__all__'
        
class LibrosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Libro
        fields = '__all__'
        
class ResenaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resena
        fields = '__all__'
        