from rest_framework import serializers
from apps.base.models.db_models import Categoria, SubCategoria


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'descripcion' : instance.descripcion,
            'sub_categoria': {
                'id' : instance.id_sub.id,
                'descripcion' : instance.id_sub.descripcion
            }
        }

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategoria
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'descripcion' : instance.descripcion
        }

