import django_filters
from apps.users.models import User

class UserFilter(django_filters.FilterSet):

    class Meta:
        model = User        
        fields = {
            'id' : ['gt','lt','exact'],
            'email' : ['contains','exact']
        }