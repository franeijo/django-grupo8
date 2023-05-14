from django.db import models

class Edificios(models.Model):
    id_edif = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=100)
    pcia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=150)

    class Meta:
        db_table = "edificios"


class UnidadFuncional(models.Model):
    TIPO_UF = [
        (1,'Departamento'),
        (2,'Cochera'),
        (3,'Local'),
        (4,'Otro'),
    ]
    id_uf = models.AutoField(primary_key=True)
    unidad_funcional = models.CharField(max_length=4)
    uf_tipo = models.IntegerField(choices=TIPO_UF,default=1)
    piso = models.CharField(max_length=10)
    dpto = models.CharField(max_length=5)
    coprop_nombre = models.CharField(max_length=150)
    porc_a = models.CharField(max_length=2, null=True)
    porc_b = models.CharField(max_length=2, null=True)
    porc_c = models.CharField(max_length=2, null=True)
    porc_d = models.CharField(max_length=2, null=True)
    edif_fk = models.ForeignKey(Edificios, on_delete=models.RESTRICT, related_name="unidad_funcional")

    class Meta:
        db_table = "unidad_funcional"


class Amenities(models.Model):
    id_ameni = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "amenities"


class EdifAmeni(models.Model):
    edi_fk = models.ForeignKey(Edificios, on_delete=models.RESTRICT, related_name="edif_ameni")
    ameni_fk = models.ForeignKey(Amenities, on_delete=models.RESTRICT, related_name="edif_ameni")

    class Meta:
        db_table = "edif_ameni"


class ReservaAmeni(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha_dde = models.DateField()
    hora_dde = models.TimeField()
    fecha_hasta = models.DateField()
    hora_hasta = models.TimeField()
    edi_fk = models.ForeignKey(Edificios, on_delete=models.RESTRICT, related_name="reserva_ameni")
    uf_fk = models.ForeignKey(UnidadFuncional, on_delete=models.RESTRICT, related_name="reserva_ameni")
    ameni_fk = models.ForeignKey(Amenities, on_delete=models.RESTRICT, related_name="reserva_ameni")

    class Meta:
        db_table = "reserva_ameni"


class ReclamosSugerencias(models.Model):
    RECLAMO_SUG = [
        (1,'Suegerencia'),
        (2,'Reclamo'),
        (3,'Felicitaciones'),
        (4,'Otro'),
    ]

    id_rec_sug = models.AutoField(primary_key=True)
    tipo_rec_sug = models.IntegerField(choices=RECLAMO_SUG,default=1)
    asunto = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    edi_fk = models.ForeignKey(Edificios, on_delete=models.RESTRICT, related_name="reclamos_sugerencias")
    uf_fk = models.ForeignKey(UnidadFuncional, on_delete=models.RESTRICT, related_name="reclamos_sugerencias", null=True)

    class Meta:
        db_table = "reclamos_sugerencias"
		
		
class Gastos(models.Model):
    TIPO_GASTO = [
        (1,'Arreglos'),
        (2,'Abonos'),
        (3,'Sueldos'),
        (4,'Insumos'),
        (5,'Suplencias'),
        (6,'Extraordinarios'),
        (7,'Otros'),
    ]

    id_gastos = models.AutoField(primary_key=True)
    tipo_gasto = models.IntegerField(choices=TIPO_GASTO,default=1)
    concepto = models.CharField(max_length=255)
    importe = models.FloatField()
    id_edificio_fk = models.ForeignKey(Edificios, on_delete=models.CASCADE, db_column='id_edificio_fk')

    class Meta:
        db_table = 'gastos'
        