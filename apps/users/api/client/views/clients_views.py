# Para los viewset
from rest_framework.response import Response
# Para usar status codes
from rest_framework import status

from rest_framework import generics

from apps.users.api.client.serializers.clients_serializers import *

from apps.users.api.client.models.models import *
from apps.users.api.filters import ClientFilter

from db_routers.permissions.db_connection import *
from apps.users.api.client.connections.clients_sp import *

import json

# LISTAR CLIENTES
class ClientListAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = ClientListSerializers
    filterset_class  = ClientFilter
    search_fields = ['nombre','id']
    ordering_fields = ['nombre','id']
    ordering = ['id']

    def get_queryset(self):
        return Persona.objects.filter(id__in = Cliente.objects.all().values_list('id', flat=True)).filter(estado = 'ACTIVO')


# BUSCAR CLIENTE
'''
class ClientRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CitySerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')
        
'''