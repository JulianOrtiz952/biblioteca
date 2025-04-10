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
        
class LibroYResenaSerializer(serializers.ModelSerializer):
    resenas = ResenaSerializer(many=True, read_only=True, source='resena_set')
    autores = serializers.StringRelatedField()
    
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autores', 'fecha_publicacion', 'resumen', 'resenas']
    