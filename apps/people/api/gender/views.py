from apps.people.api.filters import GenderFilter
from apps.people.general_serializers import GenderSerializers
from apps.people.models import Genero
from rest_framework import generics
 
class GenderAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = GenderSerializers
    filterset_class  = GenderFilter
    search_fields = ['descripcion','id']
    ordering_fields = ['descripcion','id']
    ordering = ['id']

    def get_queryset(self):
        return  Genero.objects.filter(estado = 'ACTIVO')

