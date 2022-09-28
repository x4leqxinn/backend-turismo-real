from rest_framework import serializers
from apps.base.models.db_models import Empleado
from apps.users.models import User

# Serializer para login 
class UserTokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'image','person')
    
    # Se define la data a mostrar al iniciar sesión
    def to_representation(self, instance):
        data = { 'email' : instance.email,
                'role' : {
                    'id' : instance.role.id,
                    'description' : instance.role.description
                },
                'image' : instance.image.url if instance.image != '' else '',
                'person' : instance.person.id
            }
        # TODO: Se debe indicar el id del ROLE ASIGNADO PARA LOS EMPLEADOS
        if instance.role.id == 21:
            empleado = Empleado.objects.get(id = instance.person.id)
            data['cargo'] = {
                'id' : empleado.id_car.id,
                'cargo' : empleado.id_car.descripcion
            }
        return data


