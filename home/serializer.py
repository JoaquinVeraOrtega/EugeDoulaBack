from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        #fields=('fullname','nickname')
        fields = '__all__'