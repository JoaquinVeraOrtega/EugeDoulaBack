from rest_framework import serializers
import services.models as service

class tejedoraSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.Tejedora
        fields = '__all__'

class gestarSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.GestarParirAlumbrar
        fields = '__all__'

class floresSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.Flores
        fields = '__all__'

class hierbasSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.HierbasBañosYVapores
        fields = '__all__'

class dueloSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.DueloGestacional
        fields = '__all__'

class masajeSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.Masaje
        fields = '__all__'

class cerradaSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.RitualCerrada
        fields = '__all__'

class cartografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.Cartografia
        fields = '__all__'

class alquimiaSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.Alquimia
        fields = '__all__'

class ritospasoSerializer(serializers.ModelSerializer):
    class Meta:
        model= service.RitosDePaso
        fields = '__all__'