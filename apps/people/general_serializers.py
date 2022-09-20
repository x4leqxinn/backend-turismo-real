from rest_framework import serializers
from apps.people.models import Genero, DocIdentidad, EstadoCivil


class GenderSerializers(serializers.ModelSerializer):
    # Se definen los atributos
    class Meta:
        model = Genero 
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'descripcion': instance.descripcion,
            }

class IdentificationDocumentSerializers(serializers.ModelSerializer):

    class Meta:
        model = DocIdentidad
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'descripcion': instance.descripcion,
            }


class MaritalStatusSerializers(serializers.ModelSerializer):

    class Meta:
        model = EstadoCivil
        fields = '__all__'
    
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'descripcion': instance.descripcion,
            }

