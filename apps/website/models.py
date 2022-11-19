from django.db import models

# Create your models here.

class Dataframe(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    rooms = models.TextField(blank=False)
    products = models.TextField(blank=False, null=False)
    class Meta:
        db_table = 'dataframe'
        verbose_name = "dataframe"
        verbose_name_plural = "dataframe"
        ordering = ['id']