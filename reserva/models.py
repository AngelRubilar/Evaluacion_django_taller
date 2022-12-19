from django.db import models

# Create your models here.


class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField()
    inscripcion = models.CharField(max_length=50)
    institucion = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=50)

    ESTADO_CHOICES = [
        ("d", "Disponible"),
        ("r", "Reservado"),
        ("c", "Cancelado"),
        ("a", "Anulado"),
    ]
    estado_de_reserva = models.CharField(
        max_length=1, choices=ESTADO_CHOICES, default="d"
    )
