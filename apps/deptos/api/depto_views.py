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
        