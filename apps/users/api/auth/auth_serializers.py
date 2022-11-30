from rest_framework import serializers
from apps.base.models.db_models import Empleado
from apps.users.models import User
from apps.base.models.db_models import DocIdentidad, EstadoCivil, Genero

# Serializer para login 
class UserListSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('email', 'role', 'image','person')
    
    # Se define la data a mostrar al iniciar sesión
    def to_representation(self, instance):
        data = {
                'pk' : instance.person.id,
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

from importlib.metadata import requires
from rest_framework import serializers
from apps.base.models.db_models import Cliente, Persona
from apps.users.models import User, UserRole
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth.models import Group

class ClientListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id' : instance.id.id,
            'run' : instance.id.run,
            'dv' : instance.id.dv,
            'pasaporte' : instance.id.pasaporte,
            'nombre' :instance.id.nombre,
            'snombre' :instance.id.snombre,
            'ap_paterno' :instance.id.ap_paterno,
            'ap_materno' :instance.id.ap_materno,
            'fecha_nacimiento' : instance.id.fecha_nacimiento,
            'telefono' :instance.id.telefono,
            'num_calle' :instance.id.num_calle,
            'calle' :instance.id.calle,
            'doc_identidad' : {
                'id' : instance.id.id_doc.id,
                'descripcion' : instance.id.id_doc.descripcion
            },
            'estado_civil' : {
                'id' : instance.id.id_est1.id,
                'descripcion' : instance.id.id_est1.descripcion
            },
            'genero' : {
                'id' : instance.id.id_gen.id,
                'descripcion' : instance.id.id_gen.descripcion
            }
        }



class EditAccountSerializer(serializers.Serializer):
    telefono = serializers.CharField(required=False)
    num_calle = serializers.CharField(required=False)
    calle = serializers.CharField(required=False)
    id_ciu = serializers.IntegerField(required=False)
    id_pai = serializers.IntegerField(required=False)
    id_est = serializers.IntegerField(required=False)
    id_est1 = serializers.IntegerField(required=False)
    id_gen = serializers.IntegerField(required=False)
    imagen = Base64ImageField(required=False)
    email = serializers.EmailField(required = False, max_length = 128, min_length = 5, write_only = True)
    password = serializers.CharField(required=False,max_length = 128, min_length = 5)

    def validate_email(self, value):
        value = value.lower().strip()
        exists = User.objects.filter(email=value).exists()
        if exists:
            raise serializers.ValidationError('¡El email ya se encuentra registrado!')
        return value

    def update(self, instance, validated_data):
        user = User.objects.filter(email=instance.get('email')).first()
        person = user.person
        user.email = validated_data.get('email', instance['email'])
        user.image = validated_data.get('imagen', instance['imagen'])
        if validated_data.get('password'):
            user.set_password(validated_data['password'])
        person.telefono = validated_data.get('telefono',instance['telefono'])
        person.num_calle = validated_data.get('num_calle',instance['num_calle'])
        person.calle = validated_data.get('calle',instance['calle'])
        person.id_ciu = validated_data.get('id_ciu',instance['id_ciu'])
        person.id_pai = validated_data.get('id_pais',instance['id_pai'])
        person.id_est = validated_data.get('id_est',instance['id_est'])
        person.id_est1 = EstadoCivil(id=validated_data.get('id_est1',instance['id_est1']))
        user.save()
        person.save()
        return user
