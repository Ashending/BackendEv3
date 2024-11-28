from django.db import models

# Create your models here.

class Cliente(models.Model):
    class Generos(models.TextChoices):
        FEMENINO = 'F', 'Femenino'
        MASCULINO = 'M', 'Masculino'

    class EstadoActividad(models.IntegerChoices):
        ACTIVO = 1, 'Activo'
        INACTIVO = 0, 'Inactivo'

    class Satisfaccion(models.IntegerChoices):
        PESIMO = 1, 'Pesimo'
        MALO = 2, 'Malo'
        REGULAR = 3, 'Regular'
        BUENO = 4, 'Bueno'
        EXCELENTE = 5, 'Excelente'


    id_cliente = models.BigIntegerField(primary_key=True)
    edad = models.IntegerField()
    genero = models.CharField(
        max_length=1,
        choices=Generos.choices,
    )
    saldo = models.FloatField()
    estado_actividad = models.IntegerField(choices=EstadoActividad.choices)
    nivel_satisfaccion = models.IntegerField(choices=Satisfaccion.choices)

    def __str__(self):
        return f"ID cliente: {self.id_cliente}"


