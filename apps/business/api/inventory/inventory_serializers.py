from rest_framework import serializers
from apps.base.models.db_models import DetalleProducto, DetalleSala, Inventario

class InventoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ('id',)
    
    def getProducts(self,p_id_det):
        p_queryset = DetalleProducto.objects.filter(id_det = p_id_det)
        products = []
        for index in range(len(p_queryset)):
            data = {
                'pk' : p_queryset[index].id,
                'id_producto' : p_queryset[index].id_pro.id,
                'descripcion' : p_queryset[index].id_pro.descripcion,
                'precio' : p_queryset[index].id_pro.precio,
                'estado' : {
                    'id' : p_queryset[index].id_est.id,
                    'descripcion' : p_queryset[index].id_est.descripcion
                }
            }

            products.append(data)
        return products
                


    def to_representation(self, instance):
        r_queryset = DetalleSala.objects.filter(id_inv = instance.id)
        rooms = []

        for x in range(len(r_queryset)):

            data = {
                'id' : r_queryset[x].id,
                'id_sala' : r_queryset[x].id_sal.id,
                'nombre' : r_queryset[x].id_sal.descripcion,
                'imagen' : r_queryset[x].imagen_sala.url,
                'productos' : self.getProducts(r_queryset[x].id) 
            }
            
            rooms.append(data)
    

        return {
            'id_vivienda' : instance.id_viv.id,
            'salas' : rooms
        }

