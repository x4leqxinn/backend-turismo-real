from rest_framework import serializers
from apps.base.models.db_models import Producto

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'descripcion' : instance.nombre,
            'precio' : instance.precio,
            'categoria' : {
                'id' : instance.id_cat.id,
                'descripcion' : instance.id_cat.descripcion
            }
        }