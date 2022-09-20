from django.db import models

# Create your models here.
class Genero(models.Model):
    id = models.BooleanField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'genero'
        verbose_name_plural = 'Generos'

class DocIdentidad(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'doc_identidad'
        verbose_name_plural = 'Documentos de identidad'


class EstadoCivil(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estado_civil'
        verbose_name_plural = 'Estados civiles'
