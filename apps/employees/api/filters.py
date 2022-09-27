import django_filters
from apps.base.models.db_models  import Cargo

class PositionFilter(django_filters.FilterSet):

    class Meta:
        model = Cargo
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'descripcion' : ['exact' ,'contains']
        }
