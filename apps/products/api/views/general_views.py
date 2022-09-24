from apps.products.api.filters import *
from apps.products.api.serializers.general_serializers import *
from apps.base.models.db_models import Categoria, SubCategoria
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

class SubCategoryListAPIView(generics.ListAPIView):
    serializer_class = SubCategorySerializer
    filterset_class  = SubCategoryFilter
    search_fields = ['descripcion','id']
    ordering_fields = ['descripcion','id']
    ordering = ['id','descripcion']    

    def get_queryset(self):
        return  SubCategoria.objects.filter(estado = 'ACTIVO')

class SubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')


'''
class CityListAPIView(generics.ListAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = CitySerializers
    filterset_class  = CityFilter
    search_fields = ['nombre','id']
    ordering_fields = ['nombre','id']
    ordering = ['id']

    def get_queryset(self):
        return  Ciudad.objects.filter(estado = 'ACTIVO')

class CityRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CitySerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')
        

'''