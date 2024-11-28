from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-retrieve-update-destroy'),
]
