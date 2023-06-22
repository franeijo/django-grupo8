from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Edificio(models.Model):

    PROVINCIAS = [
            (1,'Ciudad Autonoma de Buenos Aires'),
            (2,'Provincia de Buenos Aires'),
            (3,'Misiones'),
            (4,'San Luis'),
            (5,'San Juan'),
            (6,'Entre Rios'),
            (7,'Santa Cruz'),
            (8,'Rio Negro'),
            (9,'Chubut'),
            (10,'Cordoba'),
            (11,'Mendoza'),
            (12,'La Rioja'),
            (13,'Catamarca'),
            (14,'La Pampa'),
            (15,'Santiago del Estero'),
            (16,'Corrientes'),
            (17,'Santa Fe'),
            (18,'Tucuman'),
            (19,'Neuquen'),
            (20,'Chaco')
        ]

    provincia = models.IntegerField(choices=PROVINCIAS,default=1)
    ciudad = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
	
    def __str__(self):
        return self.direccion

    class Meta:
        db_table = "edificios"


class UnidadFuncional(models.Model):
    unidad_funcional = models.CharField(max_length=4)
    piso = models.CharField(max_length=10)
    dpto = models.CharField(max_length=5)
    edificio = models.ForeignKey(Edificio, on_delete=models.RESTRICT)
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT)

    class Meta:
        db_table = "unidades_funcionales"


class Amenity(models.Model):
    descripcion = models.CharField(max_length=255, null=True)
    horarios = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "amenities"


class EdificioAmenity(models.Model):
    edificio = models.ForeignKey(Edificio, on_delete=models.RESTRICT)
    amenity = models.ForeignKey(Amenity, on_delete=models.RESTRICT)

    class Meta:
        db_table = "edificios_amenities"


class Reserva(models.Model):
    fecha = models.DateField(default=datetime.now)
    horario = models.CharField()
    unidad_funcional = models.ForeignKey(UnidadFuncional, on_delete=models.RESTRICT)
    amenity = models.ForeignKey(Amenity, on_delete=models.RESTRICT)
    
    class Meta:
        db_table = "reservas"


class ReclamoSugerencia(models.Model):
    RECLAMO_SUG = [
        (1,'Sugerencia'),
        (2,'Reclamo'),
        (3,'Felicitaciones'),
        (4,'Otro'),
    ]

    tipo = models.IntegerField(choices=RECLAMO_SUG,default=1)
    asunto = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
    fecha = models.DateField(default=datetime.now)

    class Meta:
        db_table = "reclamos_sugerencias"

