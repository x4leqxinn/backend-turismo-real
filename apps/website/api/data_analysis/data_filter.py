import django_filters
from apps.website.models import Dataframe


class DataframeFilter(django_filters.FilterSet):
    class Meta:
        model = Dataframe
        
        fields = {
            'id' : ['exact'],
            'rooms' : ['contains','exact'],
            'products' : ['contains','exact'],
        }