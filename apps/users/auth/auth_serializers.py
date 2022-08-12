from rest_framework import serializers
from apps.users.models import User

# Serializer para login 
class UserTokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role')
    
    # Se define la data a mostrar al iniciar sesión
    def to_representation(self, instance):
        return {
            'email' : instance.email,
            'first_name' : instance.first_name,
            'last_name' : instance.last_name,
            'role' : {
                'id' : instance.role.id,
                'description' : instance.role.description
            }
        }



'''
'id' : instance.id,
'stock' : instance.stock.get('quantity__sum') if instance.stock.get('quantity__sum') is not None else 0,
'name' : instance.name,
'description' : instance.description,
'image' : instance.image.url if instance.image != '' else '',
'measure_unit' : instance.measure_unit.description if instance.measure_unit is not None else '',
'category' : {
    'id' : instance.category.id,
    'description' : instance.category.description
} if instance.category is not None else ''
'''
        