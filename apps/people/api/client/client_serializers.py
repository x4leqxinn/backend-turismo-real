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



class ClientCreateSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)
    email = serializers.EmailField(required = True, max_length = 128, min_length = 5, write_only = True)
    contrasenia = serializers.CharField(required=True,max_length = 40, min_length = 8, write_only = True)
    nombre = serializers.CharField(required=True,max_length = 50, min_length = 3, write_only = True)


    class Meta:
        model = Persona
        exclude = ('estado','creacion','actualizacion')

    # Custom validation
    def validate_nombre(self, value):
        value = value.upper().strip()
        return value

    def validate_ap_paterno(self, value):
        value = value.upper().strip()
        return value

    def validate_email(self, value):
        value = value.lower().strip()
        exists = User.objects.filter(email=value).exists()
        if exists:
            raise serializers.ValidationError('¡El email ya se encuentra registrado!')
        if value == '':
            raise serializers.ValidationError('Debe indicar un correo electrónico.')
        if self.validate_nombre(self.context['contrasenia']) in value:
            raise serializers.ValidationError('El email no puede contener datos de la contraseña.')
        return value


    def create(self,validated_data):
        email = validated_data.pop("email")
        contrasenia = validated_data.pop("contrasenia")
        imagen = None
        try:
            imagen = validated_data.pop("imagen")
        except:
            pass

        if validated_data['id_doc'] == 1:
            persona = Persona(**validated_data)
        else:
            persona = Persona(**validated_data)

        persona.save()
        
        cliente = Cliente(id = persona)
        cliente.save()

        # Encriptamos la contraseña
        role = UserRole.objects.get(id = 3) 
        user = User(person = persona, role = role)
        user.email = email
        user.set_password(contrasenia)
        
        # Validamos si se envía una imagen
        if imagen != None:
            user.image = imagen
        user.save()

        # TODO: Se debe crear un grupo desde el admin de DJANGO o no funcionará
        # Integrar IMAGEN
        group = Group.objects.get(id=3)
        print(group.name) 
        user.groups.add(group)
        
        # TODO: Email
        #from templates.emails.utils import sendEmailClient
        #sendEmailClient(email,'Bienvenid@ a Turismo Real',persona,'create_account/create-account.html')
        return True
