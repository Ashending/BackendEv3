from django.shortcuts import render

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cliente
from .serializers import ClienteSerializer
from .filters import ClienteFilter

"""
Vista usando django_filters para los campos 'genero', 'estado_actividad', 'nivel_satisfaccion'
"""
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClienteFilter

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

