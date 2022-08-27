from apps.locations.api.filters import CityFilter
from apps.locations.general_serializers import CitySerializers
from apps.locations.models import Ciudad
from rest_framework import generics
 
class CityListAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = CitySerializers
    filterset_class  = CityFilter
    search_fields = ['nombre','id']
    ordering_fields = ['nombre','id']
    ordering = ['id']

    def get_queryset(self):
        return  Ciudad.objects.filter(estado = 'ACTIVO')

class CityRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CitySerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')
        
