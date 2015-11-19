from django.db import models
from django.utils import timezone

class Avion(models.Model):
    Propietario = models.ForeignKey('auth.User')
    Nombre = models.CharField(max_length=50)
    TipoAvion = models.CharField(max_length=50)
    Matricula = models.CharField(max_length=50)
    Capacidad = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Aeropuerto(models.Model):
    NombreAero = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.NombreAero

class Vuelo(models.Model):
    Avion = models.ForeignKey(Avion,null=False,blank=False)
    NumeroVuelo = models.CharField(max_length=10)
    LugarDespegue = models.ForeignKey('Aeropuerto')
    LugarDestino = models.ForeignKey(Aeropuerto, related_name="Aeropuerto2")
    Pasajeros = models.CharField(max_length=50)
    fecha_vuelo = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.NumeroVuelo
