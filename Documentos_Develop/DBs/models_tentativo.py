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
    id_uf = models.AutoField(primary_key=True)
    unidad_funcional = models.CharField(max_length=4)
    uf_tipo = models.CharField(max_length=30)
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
    id_rec_sug = models.AutoField(primary_key=True)
    reclamo_sugerencia = models.CharField(max_length=100)
    asunto = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    edi_fk = models.ForeignKey(Edificios, on_delete=models.RESTRICT, related_name="reclamos_sugerencias")
    uf_fk = models.ForeignKey(UnidadFuncional, on_delete=models.RESTRICT, related_name="reclamos_sugerencias", null=True)

    class Meta:
        db_table = "reclamos_sugerencias"
