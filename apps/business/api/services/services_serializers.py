from rest_framework import serializers
from apps.base.models.db_models import DetServMov, Servicio, UbicacionTrans

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

    def to_representation(self, instance):
        # Mostrar datos según tipo de servicio
        return {
            'id' : instance.id,
            'tipo_servicio' : instance.id
        }
class LocationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UbicacionTrans
        exclude = ('creacion', 'estado', 'actualizacion')

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'nombre' : instance.nombre,
            'precio' : instance.precio,
            'tipo_ubicacion' : {
                'id' : instance.id_tip.id,
                'descripcion' : instance.id_tip.descripcion
            },
            'id_ciudad' : instance.id_ciu,
            'latitud' : instance.latitud,
            'longitud' : instance.longitud
        }


class ContactForm(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()

    def save(self):
        email = self.validated_data['email']
        message = self.validated_data['message']
        #send_email(from=email, message=message)