from rest_framework import serializers
from apps.locations.models import Pais


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
