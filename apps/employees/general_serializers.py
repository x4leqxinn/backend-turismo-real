from rest_framework import serializers
from apps.base.models.db_models import Cargo


class PositionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'descripcion': instance.descripcion,
        }


    