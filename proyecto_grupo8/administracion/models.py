from django.db import models
from django.contrib.auth.models import AbstractUser


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
    TIPO_UF = [
        (1,'Departamento'),
        (2,'Cochera'),
        (3,'Local'),
        (4,'Otro'),
    ]
    unidad_funcional = models.CharField(max_length=4)
    tipo = models.IntegerField(choices=TIPO_UF,default=1)
    piso = models.CharField(max_length=10)
    dpto = models.CharField(max_length=5)
    coprop_nombre = models.CharField(max_length=150)
    porc_a = models.CharField(max_length=2, null=True)
    porc_b = models.CharField(max_length=2, null=True)
    porc_c = models.CharField(max_length=2, null=True)
    porc_d = models.CharField(max_length=2, null=True)
    edificio = models.ForeignKey(Edificio, on_delete=models.RESTRICT)

    class Meta:
        db_table = "unidades_funcionales"


class Amenity(models.Model):
    descripcion = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "amenities"


class EdifAmeni(models.Model):
    edificio = models.ForeignKey(Edificio, on_delete=models.RESTRICT)
    amenity = models.ForeignKey(Amenity, on_delete=models.RESTRICT)

    class Meta:
        db_table = "edif_ameni"


class ReservaAmeni(models.Model):
    fecha_desde = models.DateField()
    hora_desde = models.TimeField()
    fecha_hasta = models.DateField()
    hora_hasta = models.TimeField()
    unidad_funcional = models.ForeignKey(UnidadFuncional, on_delete=models.RESTRICT)
    amenity = models.ForeignKey(Amenity, on_delete=models.RESTRICT)

    class Meta:
        db_table = "reservas"


class ReclamoSugerencia(models.Model):
    RECLAMO_SUG = [
        (1,'Suegerencia'),
        (2,'Reclamo'),
        (3,'Felicitaciones'),
        (4,'Otro'),
    ]

    tipo = models.IntegerField(choices=RECLAMO_SUG,default=1)
    asunto = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    edificio = models.ForeignKey(Edificio, on_delete=models.RESTRICT)
    unidad_funcional = models.ForeignKey(UnidadFuncional, on_delete=models.RESTRICT)

    class Meta:
        db_table = "reclamos_sugerencias"
				
class Gasto(models.Model):
    TIPO_GASTO = [
        (1,'Arreglos'),
        (2,'Abonos'),
        (3,'Sueldos'),
        (4,'Insumos'),
        (5,'Suplencias'),
        (6,'Extraordinarios'),
        (7,'Otros'),
    ]

    tipo = models.IntegerField(choices=TIPO_GASTO,default=1)
    concepto = models.CharField(max_length=255)
    importe = models.FloatField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'gastos'

class Usuario(AbstractUser):
    pass

class Perfil(models.Model):
    """MODELO QUE PERMITE DEL USER MODEL DE DJANGO PARA AGREGERLE CAMPOS EXTRAS"""
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20,verbose_name='Teléfono')
    domicilio = models.CharField(max_length=20,verbose_name='Domicilio')
    unidad_funcional = models.ForeignKey(UnidadFuncional, on_delete=models.RESTRICT)
        