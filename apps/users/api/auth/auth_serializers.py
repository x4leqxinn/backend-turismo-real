from rest_framework import serializers
from apps.base.models.db_models import Empleado
from apps.users.models import User

# Serializer para login 
class UserListSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('email', 'role', 'image','person')
    
    # Se define la data a mostrar al iniciar sesión
    def to_representation(self, instance):
        data = {
                'uid' : instance.id, 
                'email' : instance.email,
                'role' : {
                    'id' : instance.role.id,
                    'description' : instance.role.description
                },
                'image' : instance.image.url if instance.image != '' else '',
                'position' : ''
            }
        # TODO: Se debe indicar el id del ROLE ASIGNADO PARA LOS EMPLEADOS
        if instance.role.id != 3:
            empleado = Empleado.objects.get(id = instance.person.id)
            data['position'] = {
                'id' : empleado.id_car.id,
                'description' : empleado.id_car.descripcion
            }
        return data


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 128, min_length = 6, write_only = True)
    password2 = serializers.CharField(max_length = 128, min_length = 6, write_only = True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Debe ingresar ambas contraseñas iguales.'})
        return data

