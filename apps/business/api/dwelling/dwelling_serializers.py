from rest_framework import serializers
from apps.base.models.db_models import CliCom, Cliente, Comentario, GaleriaExterior, GaleriaInterior, Vivienda
from apps.users.models import User
from apps.locations.models import Cities
from drf_extra_fields.fields import Base64ImageField

class DwellingSerializer(serializers.ModelSerializer):
    # Se definen los atributos
    imagen_principal = Base64ImageField(required=False)
    class Meta:
        model = Vivienda
        fields = '__all__'

    def get_interior_galery(self, p_dwellingid):
        p_queryset = GaleriaInterior.objects.filter(id_viv = p_dwellingid)
        interiorGallery = []
        for index in range(len(p_queryset)):
            data = {
                'pk' : p_queryset[index].id,
                'imagen' : p_queryset[index].imagen.url
            }

            interiorGallery.append(data)
        return interiorGallery

    def get_exterior_gallery(self, p_dwellingid):
        p_queryset = GaleriaExterior.objects.filter(id_viv = p_dwellingid)
        exteriorGallery = []
        for index in range(len(p_queryset)):
            data = {
                'pk' : p_queryset[index].id,
                'imagen' : p_queryset[index].imagen.url
            }

            exteriorGallery.append(data)
        return exteriorGallery

    def get_comments(self, p_dwellingid):
        p_queryset = CliCom.objects.filter(id_viv = p_dwellingid)
        comments = []
        for x in range(len(p_queryset)):
            cliente = Cliente.objects.get(id=p_queryset[x].id_cli.id)
            comment = Comentario.objects.filter(id_cli=p_queryset[x].id).first()
            usuario = User.objects.filter(person__id=cliente.id.id).first()
            data = {
                'pk' : p_queryset[x].id,
                'publicacion' : comment.creacion,
                'actualizacion' : comment.actualizacion,
                'cliente' : {
                    'id' : cliente.id.id,
                    'nombre' : f'{cliente.id.nombre} {cliente.id.ap_paterno}',
                    'foto' : usuario.image.url if usuario.image else ''
                },
                'comentario' : comment.descripcion
            }
            comments.append(data)
        return comments

    def to_representation(self, instance):
        city = Cities.objects.get(id = instance.id_ciu)
        return {
            'id' : instance.id,
            'nombre' : instance.nombre,
            'descripcion' : instance.descripcion,
            'direccion' : instance.direccion,
            'imagen_principal' : instance.imagen_principal.url if instance.imagen_principal != '' else '',
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
            'capacidad' : instance.capacidad,
            'internet' : instance.internet,
            'agua' : instance.agua,
            'luz' : instance.luz,
            'gas' : instance.gas,
            'tipo_vivienda' : {
                'id' : instance.id_tip.id,
                'descripcion' : instance.id_tip.descripcion
            },
            'pais' : {
                'id' : city.country.id,
                'nombre' : city.country.name,
            },
            'estado_pais' : {
                'id' : city.state.id,
                'nombre' : city.state.name,
            },
            'ciudad' : {
                'id' : city.id,
                'nombre' : city.name
            },
            'galeria_interior' : self.get_interior_galery(instance.id),
            'galeria_exterior' : self.get_exterior_gallery(instance.id),
            'comentarios' : self.get_comments(instance.id)
        }



class CreateCommentSerializer(serializers.Serializer):
    id_cliente = serializers.IntegerField(required=True)
    id_vivienda = serializers.IntegerField(required=True)
    descripcion = serializers.CharField(max_length=100,required=True) 
    
    def validate_id_cliente(self, value):
        exists = Cliente.objects.filter(id=value)
        if not exists:
            raise serializers.ValidationError({'cliente':'El cliente no existe'})
        return exists.first()

    def validate_id_vivienda(self, value):
        exists = Vivienda.objects.filter(id=value)
        if not exists:
            raise serializers.ValidationError({'vivienda':'la vivienda no existe'})
        return exists.first()

    def create(self, validated_data):        
        detail = CliCom.objects.create(id_cli=validated_data.get('id_cliente'), id_viv=validated_data.get('id_vivienda'))
        return Comentario.objects.create(descripcion=validated_data.get('descripcion'),id_cli=detail)

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')



class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('descripcion',)

    def update(self,instance,validated_data):
        instance = Comentario.objects.get(id_cli=instance.id)
        instance.descripcion = validated_data.get('descripcion')
        instance.save()
        return instance
