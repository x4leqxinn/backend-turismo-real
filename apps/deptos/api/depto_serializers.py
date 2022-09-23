from rest_framework import serializers
from apps.base.models.db_models import Vivienda


class DeptoSerializer(serializers.ModelSerializer):
    # Se definen los atributos
    class Meta:
        model = Vivienda
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'latitud' : instance.latitud,
            'longitud' : instance.longitud,
            'estrellas' : instance.estrellas,
            'disponibilidad' : {
                'id' : instance.id_dis.id,
                'descripcion' : instance.id_dis.descripcion
            },
            'valor_noche' : instance.valor_noche,
            'abono_base' : instance.abono_base,
            'ciudad' : {
                'id' : instance.id_ciu.id,
                'nombre' : instance.id_ciu.nombre,
                'estado' : {
                    'id' : instance.id_ciu.id_est.id,
                    'nombre' : instance.id_ciu.id_est.nombre,
                    'pais' : {
                        'id' : instance.id_ciu.id_est.id_pai.id,
                        'nombre' : instance.id_ciu.id_est.id_pai.nombre
                    }
                }
            },
            'capacidad' : instance.capacidad,
            'internet' : instance.internet,
            'agua' : instance.agua,
            'luz' : instance.luz,
            'gas' : instance.gas,
            'tipo_vivienda' : {
                'id' : instance.id_tip.id,
                'descripcion' : instance.id_tip.descripcion
            }
        }