from rest_framework import serializers
from .models import Cielo

class CieloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cielo
        fields = '__all__'