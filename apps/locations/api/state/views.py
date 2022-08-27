from apps.locations.api.filters import CountryStateFilter
from apps.locations.general_serializers import CountryStateSerializers
from apps.locations.models import EstadoPais
from rest_framework import generics


class CountryStateListAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = CountryStateSerializers
    filterset_class  = CountryStateFilter
    search_fields = ['nombre','id']
    ordering_fields = ['nombre','id']
    ordering = ['id']

    def get_queryset(self):
        return  EstadoPais.objects.filter(estado = 'ACTIVO')

# Buscar País por id
class CountryStateRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CountryStateSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')
        


