# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Genero(models.Model):
    id = models.BooleanField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'genero'


class EstadoCivil(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estado_civil'


class IdentidadDoc(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'identidad_doc'


class Pais(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    cod_pais = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    cod_tel = models.CharField(max_length=10)
    bandera = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pais'



class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_est = models.ForeignKey('EstadoPais', models.DO_NOTHING, db_column='id_est')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ciudad'


class EstadoPais(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_pai = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pai')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estado_pais'


class Persona(models.Model):
    id = models.BigIntegerField(primary_key=True)
    run = models.CharField(unique=True, max_length=15, blank=True, null=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    pasaporte = models.CharField(unique=True, max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    snombre = models.CharField(max_length=50, blank=True, null=True)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    num_calle = models.CharField(max_length=10)
    calle = models.CharField(max_length=30)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_ciu = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciu')
    id_est = models.ForeignKey(EstadoPais, models.DO_NOTHING, db_column='id_est')
    id_pai = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pai')
    id_ide = models.ForeignKey(IdentidadDoc, models.DO_NOTHING, db_column='id_ide')
    id_est1 = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_est1')
    id_gen = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_gen')

    class Meta:
        managed = False
        db_table = 'persona'
