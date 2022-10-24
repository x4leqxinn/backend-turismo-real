from pyexpat import model
from rest_framework import serializers
from apps.base.models.db_models import DetServMov, Servicio

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

    def to_representation(self, instance):
        # Mostrar datos según tipo de servicio
        return {
            'id' : instance.id,
            'nombre' : instance.nombre,
            'descripcion' : instance.descripcion,
            'tipo_servicio' : instance.id
        }


class VerifyDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetServMov
        fields = ('fecha_inicio','fecha_termino')
    
    def to_representation(self, instance):
        return {
            'date_taken' : instance.fecha_inicio
        }
