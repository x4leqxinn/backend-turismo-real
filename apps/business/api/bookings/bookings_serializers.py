from pyexpat import model
from rest_framework import serializers
from apps.base.models.db_models import Persona, Reserva
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
    acompaniantes = serializers.ListField()
    class Meta:
        model = Reserva
        fields = ('fecha_inicio','fecha_termino')

    def to_representation(self, instance):
        return {
            'start' : instance.fecha_inicio,
            'end' : instance.fecha_termino,
        }


class BookingCreateSerializer(serializers.ModelSerializer):

    acompaniantes = serializers.ListField()
    class Meta:
        model = Reserva
        exclude = ('estado','creacion','actualizacion')

    def validate_acompaniantes(self, values):
        if len(values) > 0:
            # Verificamos que tenga el formato correcto
            try:
                for index in range(len(values)):
                    values[index]["run"]
                    values[index]["dv"]
                    values[index]["pasaporte"]
                    values[index]["nombre"]
                    values[index]["snombre"]
                    values[index]["ap_paterno"]
                    values[index]["ap_materno"]
                    values[index]["fecha_nacimiento"]
                    values[index]["telefono"]
                    values[index]["num_calle"]
                    values[index]["calle"]
                    values[index]["id_ciu"]
                    values[index]["id_est"]
                    values[index]["id_pai"]
                    values[index]["id_doc"]
                    values[index]["id_est1"]
                    values[index]["id_gen"]
            except:
                raise serializers.ValidationError('¡Acompañante en mal formato!')

        return values

    def create(self,validated_data):

        print('OLA', validated_data['acompaniantes'])
        
        
        return True
