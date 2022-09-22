import django_filters
from apps.users.api.client.models.db_models import *

class ClientFilter(django_filters.FilterSet):

    class Meta:
        model = Persona
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','exact'],
            'run' : ['gt','lt','contains','exact'],
            'dv' : ['gt','lt','contains','exact'],
            'pasaporte' : ['gt','lt','contains','exact'], 
            'nombre' : ['exact' ,'contains'],
            'snombre' : ['exact' ,'contains'],
            'ap_paterno' : ['exact' ,'contains'],
            'ap_materno' : ['exact' ,'contains'],
            'fecha_nacimiento' : ['exact' ,'contains'],
            'telefono' : ['exact' ,'contains'],
            'num_calle' : ['exact' ,'contains'],
            'calle' : ['exact' ,'contains'],
            'id_ciu' : ['gt','lt','exact'],
            'id_est' : ['gt','lt','exact'],
            'id_pai' : ['gt','lt','exact'],
            'id_doc' : ['gt','lt','exact'],
            'id_est1' : ['gt','lt','exact'],
            'id_gen' : ['gt','lt','exact']
        }
            