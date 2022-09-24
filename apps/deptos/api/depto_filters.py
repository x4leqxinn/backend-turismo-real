import django_filters
from apps.base.models.db_models import DetalleProducto, DetalleSala, EstadoProducto, GaleriaExterior, GaleriaInterior, Sala, Vivienda, Comentario
class DeptoFilter(django_filters.FilterSet):

    class Meta:
        model = Vivienda
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'latitud' : ['exact' ,'contains'],
            'longitud' : ['exact' ,'contains'],
            'estrellas' : ['exact' ,'contains'],
            'id_dis__descripcion' : ['exact' ,'contains'],
            'valor_noche' : ['exact' ,'contains'],
            'id_ciu__nombre' : ['exact' ,'contains'],
            'id_ciu__id_est__nombre' : ['exact' ,'contains'],
            'id_ciu__id_est__id_pai__nombre' : ['exact' ,'contains'],
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
            'imagen' : ['contains','exact'],
            'id_viv__id' : ['gt','lt','contains','exact'],
        }


class ExteriorFilter(django_filters.FilterSet):
    class Meta:
        model = GaleriaExterior
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'imagen' : ['contains','exact'],
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
            'id' : ['gt','lt','contains','exact']
        }

class RoomDetailFilter(django_filters.FilterSet):
    class Meta: 
        model = DetalleSala
        fields = {
            'id' : ['gt','lt','contains','exact']
        }