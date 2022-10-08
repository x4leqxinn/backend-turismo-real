import django_filters
from apps.locations.models import Countries, States, Cities

class CountryFilter(django_filters.FilterSet):

    class Meta:
        model = Countries
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'name' : ['exact' ,'contains']
        }
            
class CountryStateFilter(django_filters.FilterSet):

    class Meta:
        model = States
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact']
        }

class CityFilter(django_filters.FilterSet):

    class Meta:
        model = Cities
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact']
        }