from pyexpat import model
from rest_framework import serializers
from apps.base.models.db_models import Reserva
from apps.locations.models import Cities


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')

    def to_representation(self, instance):
        city = Cities.objects.get(id = instance.id_viv.id_ciu)
        return {
            'id' : instance.id,
            # TODO: Hay que serializar el modelo persona
            'cliente' : {
                #'id' : instance.id_cli.id
            },
            'vivienda' : {
                'id' : instance.id_viv.id,
                'tipo_vivienda' : {
                    'id' : instance.id_viv.id_tip.id,
                    'descripcion' : instance.id_viv.id_tip.descripcion
                },
                'nombre' : instance.id_viv.nombre,
                'descripcion' : instance.id_viv.descripcion,
                'valor_noche' : instance.id_viv.valor_noche,
                'direccion' : instance.id_viv.direccion,
                'pais' : {
                    'id' : city.country.id,
                    'nombre' : city.country.name,
                },
                'estado_pais' : {
                    'id' : city.state.id,
                    'nombre' : city.state.name,
                },
                'ciudad' : {
                    'id' : city.id,
                    'nombre' : city.name
                },
            }
        }

class BookingDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('fecha_inicio','fecha_termino')

    def to_representation(self, instance):
        return {
            'start' : instance.fecha_inicio,
            'end' : instance.fecha_termino,
        }