from re import I
from rest_framework import serializers
from apps.base.models.db_models import Comentario, DetalleProducto, EstadoProducto, GaleriaExterior, GaleriaInterior, Sala, Vivienda


class DeptoSerializer(serializers.ModelSerializer):
    # Se definen los atributos
    class Meta:
        model = Vivienda
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'nombre' : instance.nombre,
            'descripcion' : instance.descripcion,
            'direccion' : instance.direccion,
            'imagen_principal' : instance.imagen_principal,
            'slug' : instance.slug,
            'latitud' : instance.latitud,
            'longitud' : instance.longitud,
            'estrellas' : instance.estrellas,
            'disponibilidad' : {
                'id' : instance.id_dis.id,
                'descripcion' : instance.id_dis.descripcion
            },
            'valor_noche' : instance.valor_noche,
            'abono_base' : instance.abono_base,
            'ciudad' : {
                'id' : instance.id_ciu.id,
                'nombre' : instance.id_ciu.nombre,
                'estado' : {
                    'id' : instance.id_ciu.id_est.id,
                    'nombre' : instance.id_ciu.id_est.nombre,
                    'pais' : {
                        'id' : instance.id_ciu.id_est.id_pai.id,
                        'nombre' : instance.id_ciu.id_est.id_pai.nombre
                    }
                }
            },
            'capacidad' : instance.capacidad,
            'internet' : instance.internet,
            'agua' : instance.agua,
            'luz' : instance.luz,
            'gas' : instance.gas,
            'tipo_vivienda' : {
                'id' : instance.id_tip.id,
                'descripcion' : instance.id_tip.descripcion
            },
        }

class InteriorGalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GaleriaInterior
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'imagen' : instance.imagen
        }

class ExteriorGalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GaleriaExterior
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'imagen' : instance.imagen
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'comentario' : instance.descripcion,
            'cliente': {
                'id' : instance.id_cli.id_cli.id.id,
                'nombre' : instance.id_cli.id_cli.id.nombre + ' ' + instance.id_cli.id_cli.id.ap_paterno + ' ' + instance.id_cli.id_cli.id.ap_materno
            },
            'id_vivienda' : instance.id_cli.id_viv.id
        }

class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sala
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'sala' : instance.descripcion
        }

class ProductStateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EstadoProducto
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'estado' : instance.descripcion
        }

class ProductDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DetalleProducto
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'id_est' : instance.id_est.id,
            'id_det' : instance.id_det.id,
            'id_pro' : instance.id_pro.id
        }

class RoomDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DetalleProducto
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'id_inv' : instance.id_inv.id,
            'id_sal' : instance.id_sal.id
        }
