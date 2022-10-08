from apps.business.api.general_filters import *
from apps.business.api.inventory.inventory_serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

'''
class DeptoListAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = DeptoSerializer
    filterset_class  = DeptoFilter
    search_fields = ['id','id_dis__descripcion','id_ciu__nombre','id_ciu__id_est__nombre','id_ciu__id_est__id_pai__nombre']
    ordering_fields = ['gas','luz','agua','internet','capacidad','abono_base','valor_noche','estrellas','id']
    ordering = ['id']

    def get_queryset(self):
        return  Vivienda.objects.filter(estado = 'ACTIVO')

class DeptoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DeptoSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')
        
class InteriorGaleryListAPIView(generics.ListAPIView):
    serializer_class = InteriorGalerySerializer
    filterset_class  = InteriorFilter
    search_fields = ['id_viv__id']
    ordering_fields = ['id','id_viv__id']
    ordering = ['id','id_viv__id']

    def get_queryset(self):
        return  GaleriaInterior.objects.filter(estado = 'ACTIVO')
class ExteriorGaleryListAPIView(generics.ListAPIView):
    serializer_class = ExteriorGalerySerializer
    filterset_class  = ExteriorFilter
    search_fields = ['id_viv__id']
    ordering_fields = ['id','id_viv__id']
    ordering = ['id','id_viv__id']

    def get_queryset(self):
        return  GaleriaExterior.objects.filter(estado = 'ACTIVO')
class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    filterset_class  = CommentFilter
    search_fields = ['id_cli__id_viv__id']
    ordering_fields = ['id','id_cli__id_cli__id__id','id_cli__id_viv__id']
    ordering = ['id','id_cli__id_viv__id']

    def get_queryset(self):
        return Comentario.objects.filter(estado = 'ACTIVO')

class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer
    filterset_class  = RoomFilter
    search_fields = ['id','descripcion']
    ordering_fields = ['id', 'descripcion']
    ordering = ['id']

    def get_queryset(self):
        return Sala.objects.filter(estado = 'ACTIVO')

class ProductStateListAPIView(generics.ListAPIView):
    serializer_class = ProductStateSerializer
    filterset_class  = ProductStateFilter
    search_fields = ['id','descripcion']
    ordering_fields = ['id', 'descripcion']
    ordering = ['id']

    def get_queryset(self):
        return EstadoProducto.objects.filter(estado = 'ACTIVO')

'''
class InventoryViewSet(viewsets.GenericViewSet):
    serializer_class = InventoryListSerializer
    filterset_class  = InventoryFilter
    search_fields = ['id_viv__id']
    ordering_fields = ['id']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ["create"]:
            return None
        elif self.action in ["list"]:
            return InventoryListSerializer
        return self.serializer_class

    def get_queryset(self):
        return Inventario.objects.filter(estado = 'ACTIVO')

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
        queryset = Inventario.objects.filter(estado = 'ACTIVO')
        employee = get_object_or_404(queryset, pk=pk)
        serializer = InventoryListSerializer(employee)
        return Response(serializer.data)
