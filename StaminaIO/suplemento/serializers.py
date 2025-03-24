from rest_framework import serializers
from .models import Suplemento

class SuplementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suplemento
        fields = '__all__' 
