from unittest.util import _MAX_LENGTH
from rest_framework import serializers



class ClientSerializers(serializers.Serializer):
    # Se definen los atributos
    resultado = serializers.CharField(max_length = 255)

    def to_representation(self, instance):
        return {'resultado' : instance.resultado}
