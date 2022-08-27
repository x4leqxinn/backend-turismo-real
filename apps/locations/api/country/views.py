from apps.locations.api.filters import CountryFilter
from apps.locations.general_serializers import CountrySerializers
from apps.locations.models import Pais
from rest_framework import generics


# Listar Paises con filtros 
class CountryListAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = CountrySerializers
    filterset_class  = CountryFilter
    search_fields = ['nombre','id']
    ordering_fields = ['nombre','cod_tel','cod_pais','id']
    ordering = ['id']

    def get_queryset(self):
        return  Pais.objects.filter(estado = 'ACTIVO')

# Buscar País por id
class CountryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CountrySerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')
        
