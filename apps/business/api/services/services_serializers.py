from rest_framework import serializers
from apps.base.models.db_models import Servicio

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
        }

