import django_filters
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    genero = django_filters.CharFilter(field_name='genero', lookup_expr='iexact')
    estado_actividad = django_filters.ChoiceFilter(choices=Cliente.EstadoActividad.choices)
    nivel_satisfaccion = django_filters.ChoiceFilter(choices=Cliente.Satisfaccion.choices)

    class Meta:
        model = Cliente
        fields = ['genero', 'estado_actividad', 'nivel_satisfaccion']
