import django_filters
from apps.base.models.db_models import DetalleProducto, DetalleSala, EstadoProducto, GaleriaExterior, GaleriaInterior, Inventario, Sala, Vivienda, Comentario


class DwellingFilter(django_filters.FilterSet):

    class Meta:
        model = Vivienda
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'latitud' : ['exact' ,'contains'],
            'longitud' : ['exact' ,'contains'],
            'estrellas' : ['exact' ,'contains'],
            'id_dis__descripcion' : ['exact' ,'contains'],
            'id_ciu' : ['exact'],
            'valor_noche' : ['exact' ,'contains'],
            'capacidad' : ['exact' ,'contains'],
            'internet' : ['exact' ,'contains'],
            'luz' : ['exact' ,'contains'],
            'agua' : ['exact' ,'contains'],
            'gas' : ['exact' ,'contains']
        }

class InteriorFilter(django_filters.FilterSet):
    class Meta:
        model = GaleriaInterior
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'id_viv__id' : ['gt','lt','contains','exact'],
        }


class ExteriorFilter(django_filters.FilterSet):
    class Meta:
        model = GaleriaExterior
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'id_viv__id' : ['gt','lt','contains','exact'],
        }

class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comentario
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'descripcion' : ['contains','exact'],
            'id_cli__id_cli__id__nombre' : ['contains','exact'],
            'id_cli__id_cli__id__id' : ['gt','lt','contains','exact'],
            'id_cli__id_viv__id' : ['gt','lt','contains','exact']
        }

class RoomFilter(django_filters.FilterSet):
    class Meta: 
        model = Sala
        fields = {
            'id' : ['gt','lt','contains','exact']
        }

class ProductStateFilter(django_filters.FilterSet):
    class Meta: 
        model = EstadoProducto
        fields = {
            'id' : ['gt','lt','contains','exact']
        }


class ProductDetailFilter(django_filters.FilterSet):
    class Meta: 
        model = DetalleProducto
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'id_det__id_sal__id' : ['contains','exact'],
            'id_det__id_sal__descripcion' : ['contains','exact'],
            'id_det__id_inv__id_viv__id' : ['contains','exact']
        }

class RoomDetailFilter(django_filters.FilterSet):
    class Meta: 
        model = DetalleSala
        fields = {
            'id' : ['gt','lt','contains','exact']
        }
        

class InventoryFilter(django_filters.FilterSet):
    class Meta: 
        model = Inventario
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'id_viv__id' : ['gt','lt','contains','exact']
        }