from django.db import models
from apps.base.models.base_model import BaseModel
# Create your models here.
class CuentaBancaria(BaseModel):
    cvv = models.CharField(null=False, blank=False, max_length=3)
    fecha_expiracion = models.CharField(null=False, blank=False, max_length=5)
    nombre_titular = models.CharField(null=False, blank=False, max_length=200)
    numero_cuenta = models.CharField(null=False, blank=False, unique=True, max_length=100)
    persona_id = models.OneToOneField('people.Persona', models.DO_NOTHING, db_column='persona_id')

    class Meta:
        managed = True
        db_table = "cuenta_bancaria"
        verbose_name = "Cuenta bancaria"
        verbose_name_plural = "Cuentas bancarias"
        ordering = ['id']