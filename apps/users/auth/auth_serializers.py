from rest_framework import serializers
from apps.users.models import User

# Serializer para login 
class UserTokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'image')
    
    # Se define la data a mostrar al iniciar sesión
    def to_representation(self, instance):
        return {
            'email' : instance.email,
            'role' : {
                'id' : instance.role.id,
                'description' : instance.role.description
            },
            'image' : instance.image.url if instance.image != '' else ''
        }


