import django_filters
from apps.locations.models import *

class CountryFilter(django_filters.FilterSet):

    class Meta:
        model = Pais
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'cod_pais' : ['exact' ,'contains'],
            'nombre' : ['exact' ,'contains'],
            'cod_tel' : ['exact' ,'contains'],
            'bandera' : ['exact' ,'contains']
        }
            