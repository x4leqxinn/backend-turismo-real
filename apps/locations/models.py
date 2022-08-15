from django.db import models

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    id_oun = models.ForeignKey('CountryState', models.DO_NOTHING, db_column='id_oun')

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    sortname = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    phonecode = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'country'


class CountryState(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    id_oun = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_oun')

    class Meta:
        managed = False
        db_table = 'country_state'
