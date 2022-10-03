from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=15, null=False, blank=False, default='ACTIVO')
    creacion = models.DateField('Fecha de Creación',auto_now=False, auto_now_add=True)
    actualizacion = models.DateField('Fecha de Actualización', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'