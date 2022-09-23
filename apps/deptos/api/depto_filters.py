import django_filters
from apps.base.models.db_models import Vivienda

class DeptoFilter(django_filters.FilterSet):

    class Meta:
        model = Vivienda
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'latitud' : ['exact' ,'contains'],
            'longitud' : ['exact' ,'contains'],
            'estrellas' : ['exact' ,'contains'],
            'id_dis__descripcion' : ['exact' ,'contains'],
            'valor_noche' : ['exact' ,'contains'],
            'id_ciu__nombre' : ['exact' ,'contains'],
            'id_ciu__id_est__nombre' : ['exact' ,'contains'],
            'id_ciu__id_est__id_pai__nombre' : ['exact' ,'contains'],
            'capacidad' : ['exact' ,'contains'],
            'internet' : ['exact' ,'contains'],
            'luz' : ['exact' ,'contains'],
            'agua' : ['exact' ,'contains'],
            'gas' : ['exact' ,'contains']
        }
            

