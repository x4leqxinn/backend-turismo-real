from apps.products.api.filters import *
from rest_framework import generics
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filterset_class  = ProductFilter
    search_fields = ['nombre','id']
    ordering_fields = ['nombre','id']
    ordering = ['id','nombre']    

    def get_queryset(self):
        return Producto.objects.filter(estado = 'ACTIVO')

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')

