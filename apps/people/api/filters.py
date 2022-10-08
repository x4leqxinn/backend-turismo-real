import django_filters
from apps.base.models.db_models import *


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Empleado
        #fields = ('description',)
        
        fields = {
            'id__id' : ['gt','lt','exact'],
            'id__run' : ['gt','lt','contains','exact'],
            'id__dv' : ['gt','lt','contains','exact'],
            'id__pasaporte' : ['gt','lt','contains','exact'], 
            'id__nombre' : ['exact' ,'contains'],
            'id__snombre' : ['exact' ,'contains'],
            'id__ap_paterno' : ['exact' ,'contains'],
            'id__ap_materno' : ['exact' ,'contains'],
            'id__fecha_nacimiento' : ['exact' ,'contains'],
            'id__telefono' : ['exact' ,'contains'],
            'id__num_calle' : ['exact' ,'contains'],
            'id__calle' : ['exact' ,'contains'],
            'id__id__id_ciu' : ['gt','lt','exact'],
            'id__id_est' : ['gt','lt','exact'],
            'id__id_pai' : ['gt','lt','exact'],
            'id__id_doc' : ['gt','lt','exact'],
            'id__id_est1' : ['gt','lt','exact'],
            'id__id_gen' : ['gt','lt','exact'],
            'sueldo':['gt','lt','exact'],
            'fecha_contrato' :['exact' ,'contains'],
            'id_car':['gt','lt','exact']
        }

