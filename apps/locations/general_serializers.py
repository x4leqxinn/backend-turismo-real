from rest_framework import serializers
from apps.locations.models import Country


class CountrySerializers(serializers.ModelSerializer):
    # Se definen los atributos
    class Meta:
        model = Country 
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'sortname': instance.sortname,
            'name' : instance.name,
            'phonecode' : instance.phonecode,
            }
