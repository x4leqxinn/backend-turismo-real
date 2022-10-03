from apps.people.api.filters import IdentificationDocumentFilter
from apps.people.general_serializers import IdentificationDocumentSerializers
from apps.base.models.db_models import *
from rest_framework import generics
 
class IdentificationDocumentAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = IdentificationDocumentSerializers
    filterset_class  = IdentificationDocumentFilter
    search_fields = ['descripcion','id']
    ordering_fields = ['descripcion','id']
    ordering = ['id']

    def get_queryset(self):
        return  DocIdentidad.objects.filter(estado = 'ACTIVO')

