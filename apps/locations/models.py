from tabnanny import verbose
from django.db import models


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
        verbose_name_plural = 'Ciudades'


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
        verbose_name_plural = 'Países'



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
        verbose_name_plural = 'Estados de países'