from apps.people.api.filters import MaritalStatusFilter
from apps.people.general_serializers import MaritalStatusSerializers
from apps.people.models import EstadoCivil
from rest_framework import generics
 
class MaritalStatusAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = MaritalStatusSerializers
    filterset_class  = MaritalStatusFilter
    search_fields = ['descripcion','id']
    ordering_fields = ['descripcion','id']
    ordering = ['id']

    def get_queryset(self):
        return  EstadoCivil.objects.filter(estado = 'ACTIVO')

