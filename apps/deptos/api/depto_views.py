from apps.deptos.api.depto_filters import *
from apps.deptos.api.depto_serializers import *
from apps.base.models.db_models import Vivienda
from rest_framework import generics


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