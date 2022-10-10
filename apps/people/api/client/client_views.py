from multiprocessing import context
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.base.models.db_models import Cliente
from apps.people.api.client.client_serializers import *
from apps.people.api.filters import ClientFilter

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
        return Cliente.objects.filter(id__estado = 'ACTIVO')


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
        serializer = self.serializer_class(data = request.data, context = request.data) # Aquí enviariamos el resultado de data
        if serializer.is_valid():
            if serializer.save(): 
                return Response({'message' : 'Cliente registrado correctamente.'}, status = status.HTTP_201_CREATED)
        return Response(
            {
                'message' : 'Hay errores en la creación.',
                'errors' : serializer.errors
            }
            , status = status.HTTP_400_BAD_REQUEST)