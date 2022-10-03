from apps.products.api.filters import *
from apps.products.api.serializers.general_serializers import *
from apps.base.models.db_models import Categoria
from rest_framework import generics

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    filterset_class  = CategoryFilter
    search_fields = ['descripcion','id']
    ordering_fields = ['descripcion','id']
    ordering = ['id','descripcion']    

    def get_queryset(self):
        return  Categoria.objects.filter(estado = 'ACTIVO')

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')
