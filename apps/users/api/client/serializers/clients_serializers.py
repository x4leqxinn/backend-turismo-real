from rest_framework import serializers
from apps.users.api.client.connections.clients_sp import createClient
from apps.users.api.client.models.db_models import *
from apps.users.api.client.models.models import Client
from db_routers.permissions.db_connection import oracle_connection

class ClientListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'run' : instance.run,
            'dv' : instance.dv,
            'pasaporte' : instance.pasaporte,
            'nombre' :instance.nombre,
            'snombre' :instance.snombre,
            'ap_paterno' :instance.ap_paterno,
            'ap_materno' :instance.ap_materno,
            'fecha_nacimiento' : instance.fecha_nacimiento,
            'telefono' :instance.telefono,
            'num_calle' :instance.num_calle,
            'calle' :instance.calle,
            'pais' : {
                'id' : instance.id_pai.id,
                'nombre' : instance.id_pai.nombre,
            },
            'id_est' : {
                'id' : instance.id_est.id,
                'nombre' : instance.id_est.nombre,
            },
            'id_ciu' : {
                'id' : instance.id_ciu.id,
                'nombre' : instance.id_ciu.nombre
            },
            'doc_identidad' : {
                'id' : instance.id_doc.id,
                'descripcion' : instance.id_doc.descripcion
            },
            'estado_civil' : {
                'id' : instance.id_est1.id,
                'descripcion' : instance.id_est1.descripcion
            },
            'genero' : {
                'id' : instance.id_gen.id,
                'descripcion' : instance.id_gen.descripcion
            }
        }



class ClientCreateSerializer(serializers.Serializer):
    rut = serializers.CharField(max_length=20)
    dv = serializers.CharField(max_length=1)
    pasaporte = serializers.CharField(max_length=20)
    nombre = serializers.CharField(max_length=100)
    snombre = serializers.CharField(max_length=100)
    ap_paterno = serializers.CharField(max_length=100)
    ap_materno = serializers.CharField(max_length=100)
    fecha_nacimiento = serializers.CharField(max_length=20)
    telefono = serializers.CharField(max_length=20)
    num_calle = serializers.CharField(max_length=10)
    calle = serializers.CharField(max_length=20)
    correo = serializers.CharField(max_length=100)
    id_ciu = serializers.IntegerField()
    id_est = serializers.IntegerField()
    id_pai = serializers.IntegerField()
    id_doc = serializers.IntegerField()
    id_est_civ = serializers.IntegerField()
    id_gen = serializers.IntegerField()

    def create(self,validated_data):
        print(validated_data)
        cliente = Client(validated_data['rut'],validated_data['dv'],validated_data['pasaporte'],
        validated_data['nombre'],validated_data['snombre'],validated_data['ap_paterno'],
        validated_data['ap_materno'],validated_data['fecha_nacimiento'],validated_data['telefono'],
        validated_data['num_calle'],validated_data['calle'],validated_data['id_ciu'],
        validated_data['id_est'],validated_data['id_pai'],validated_data['id_doc'],validated_data['id_est_civ'],
        validated_data['id_gen'])
        from templates.emails.utils import sendEmailClient
        sendEmailClient(validated_data['correo'],'Bienvenid@ a Turismo Real',cliente,'create_account/create-account.html')
        # Llamar al SP
        return createClient(oracle_connection(1),cliente) 