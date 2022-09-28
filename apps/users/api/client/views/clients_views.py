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

from rest_framework import viewsets
from rest_framework.decorators import action

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

# GENERIC VIEWSET (Permite todos los métodos en una url)
class ClientViewSet(viewsets.GenericViewSet):
    # model = Cliente
    serializer_class = ClientCreateSerializer
    filterset_class  = ClientFilter
    search_fields = ['nombre','id']
    ordering_fields = ['nombre','id']
    ordering = ['id']


    def get_serializer_class(self):
        if self.action in ["create"]:
            return ClientCreateSerializer
        elif self.action in ["list"]:
            return ClientListSerializers
        return self.serializer_class


    def get_queryset(self):
        return Persona.objects.filter(id__in = Cliente.objects.all().values_list('id', flat=True)).filter(estado = 'ACTIVO')


    def list(self, request):
        # with filter
        queryset = self.filter_queryset(self.get_queryset())

        # pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data = request.data) # Aquí enviariamos el resultado de data
        if serializer.is_valid():
            if serializer.save(): 
                return Response({'message' : 'Cliente registrado correctamente.'}, status = status.HTTP_201_CREATED)
            return Response({'error' : 'Datos inválidos'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)