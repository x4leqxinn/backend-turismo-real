from rest_framework import serializers
from apps.locations.models import Pais, EstadoPais, Ciudad


class CountrySerializers(serializers.ModelSerializer):
    # Se definen los atributos
    class Meta:
        model = Pais 
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'abreviacion': instance.cod_pais,
            'nombre' : instance.nombre,
            'prefijo' : instance.cod_tel,
            'bandera' : instance.bandera
            }

class CountryStateSerializers(serializers.ModelSerializer):

    class Meta:
        model = EstadoPais
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'nombre' : instance.nombre,
            'pais' : {
                'id' : instance.id_pai.id,
                'nombre' : instance.id_pai.nombre
            }
        }


class CitySerializers(serializers.ModelSerializer):

    class Meta:
        model = Ciudad
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'nombre' : instance.nombre,
            'estado' : {
                'id' : instance.id_est.id,
                'nombre' : instance.id_est.nombre,
                'pais' : {
                    'id' : instance.id_est.id_pai.id,
                    'nombre' : instance.id_est.id_pai.nombre
                }
            }
        }

