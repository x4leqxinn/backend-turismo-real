from rest_framework import serializers
from apps.users.api.client.models.db_models import *

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


'''
'id' : instance.id,
            'nombre' : instance.nombre,
            'pais' : {
                'id' : instance.id_pai.id,
                'nombre' : instance.id_pai.nombre
            }
'''

