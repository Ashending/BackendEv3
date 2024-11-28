from rest_framework import serializers
from .models import Cliente

"""
clase para serializar todos los campos del modelo Cliente
"""
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


