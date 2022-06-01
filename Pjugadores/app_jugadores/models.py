from django.db import models

# Create your models here.

class Jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    equipo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f'Jugador -- {self.nombre}'


class Club(models.Model):
    nombre = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    localidad = models.CharField(max_length=30)

    def __str__(self):
        return f'Club: {self.nombre} -- Provincia: {self.provincia} -- Localidad: {self.localidad}'


class Liga(models.Model):
    torneo = models.CharField(max_length=40)
    equipos = models.IntegerField()
    internacional = models.BooleanField()
    
    def __str__(self):
        es_internacional = 'Si' if self.internacional else 'No'
        return f'Torneo: {self.torneo} -- Internacional: {es_internacional}'