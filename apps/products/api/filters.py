import django_filters
from apps.base.models.db_models import Categoria, Producto


class CategoryFilter(django_filters.FilterSet):

    class Meta:
        model = Categoria
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'descripcion' : ['exact' ,'contains'],
        }
class ProductFilter(django_filters.FilterSet):
    
    class Meta: 
        models = Producto
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'nombre' : ['exact' ,'contains']
        }