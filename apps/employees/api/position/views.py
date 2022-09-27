from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from apps.employees.general_serializers import PositionSerializers
from rest_framework import viewsets
from apps.employees.api.filters import PositionFilter
from apps.base.models.db_models import Cargo


class PositionViewSet(viewsets.GenericViewSet):
    serializer_class = PositionSerializers
    filterset_class  = PositionFilter
    search_fields = ['descripcion','id']
    ordering_fields = ['descripcion','id']
    ordering = ['id']


    
    def get_queryset(self):
        return Cargo.objects.filter(estado = 'ACTIVO')



    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)