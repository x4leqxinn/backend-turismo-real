from apps.business.api.general_filters import DwellingFilter
from apps.business.api.dwelling.dwelling_serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from apps.base.stored_procedures import genericDelete
from db_routers.permissions.db_connection import oracle_connection

class DwellingViewSet(viewsets.GenericViewSet):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = DwellingSerializer
    filterset_class  = DwellingFilter
    search_fields = ['id','id_dis__descripcion','id_ciu__nombre','id_ciu__id_est__nombre','id_ciu__id_est__id_pai__nombre']
    ordering_fields = ['gas','luz','agua','internet','capacidad','abono_base','valor_noche','estrellas','id']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ["create"]:
            return None
        elif self.action in ["list"]:
            return DwellingSerializer
        return self.serializer_class

    def get_queryset(self):
        return Vivienda.objects.filter(estado = 'ACTIVO')

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

    def retrieve(self, request, pk=None):
        queryset = Vivienda.objects.filter(estado = 'ACTIVO')
        dwelling = get_object_or_404(queryset, pk=pk)
        serializer = DwellingSerializer(dwelling)
        return Response(serializer.data)

    def destroy(self, request, pk = None):
        dwelling = self.get_queryset().filter(id = pk).first()
        if dwelling and genericDelete(oracle_connection(1),pk,'VIVIENDA') == 1: 
            return Response({'message':'Vivienda eliminada correctamente.'}, status = status.HTTP_200_OK)
        return Response({'Error' :  '¡No existe una vivienda con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
