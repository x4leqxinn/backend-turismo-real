from rest_framework import serializers
from apps.base.models.db_models import CliCom, Cliente, Comentario, GaleriaExterior, GaleriaInterior, Vivienda
from apps.locations.models import Cities
from drf_extra_fields.fields import Base64ImageField

class DwellingSerializer(serializers.ModelSerializer):
    # Se definen los atributos
    imagen_principal = Base64ImageField(required=False)
    class Meta:
        model = Vivienda
        fields = '__all__'

    def getInteriorGallery(self, p_dwellingid):
        p_queryset = GaleriaInterior.objects.filter(id_viv = p_dwellingid)
        interiorGallery = []
        for index in range(len(p_queryset)):
            data = {
                'pk' : p_queryset[index].id,
                'imagen' : p_queryset[index].imagen.url
            }

            interiorGallery.append(data)
        return interiorGallery

    def getExteriorGallery(self, p_dwellingid):
        p_queryset = GaleriaExterior.objects.filter(id_viv = p_dwellingid)
        exteriorGallery = []
        for index in range(len(p_queryset)):
            data = {
                'pk' : p_queryset[index].id,
                'imagen' : p_queryset[index].imagen.url
            }

            exteriorGallery.append(data)
        return exteriorGallery

    def getComments(self, p_dwellingid):
        p_queryset = CliCom.objects.filter(id_viv = p_dwellingid)
        comments = []
        for x in range(len(p_queryset)):
            p_queryset2 = Comentario.objects.filter(id = p_queryset[x].id)
            clientes = Cliente.objects.get(id = p_queryset[x].id_cli.id)
            
            # Revisar
            print(clientes.id)

            for index in range(len(p_queryset2)):
                data = {
                    'pk' : p_queryset2[index].id,
                    # TODO: Arreglar llamado a cliente, se puede intentar serializar
                    'id_cliente' : str(clientes.id.id),
                    'cliente' : str(clientes.id.nombre),
                    'comentario' :p_queryset2[index].descripcion
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
            'imagen_principal' : instance.imagen_principal.url,
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
            'galeria_interior' : self.getInteriorGallery(instance.id),
            'galeria_exterior' : self.getExteriorGallery(instance.id),
            'comentarios' : self.getComments(instance.id)
        }
