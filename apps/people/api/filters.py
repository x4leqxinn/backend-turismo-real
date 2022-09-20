import django_filters
from apps.people.models import *

class GenderFilter(django_filters.FilterSet):

    class Meta:
        model = Genero
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'descripcion' : ['exact' ,'contains']
        }
            
class IdentificationDocumentFilter(django_filters.FilterSet):

    class DocIdentidad:
        model = DocIdentidad
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'descripcion' : ['exact' ,'contains']
        }

class MaritalStatusFilter(django_filters.FilterSet):

    class Meta:
        model = EstadoCivil
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'descripcion' : ['exact' ,'contains']
        }