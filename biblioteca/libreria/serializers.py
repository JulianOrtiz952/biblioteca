from rest_framework import serializers
from libreria.models import Autor

class AutoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Autor
        fields = '__all__'
        