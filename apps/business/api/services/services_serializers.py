from rest_framework import serializers
from apps.base.models.db_models import DetServMov, Servicio, UbicacionTrans, Cliente, Conductor, DetServMov,Tour, Servicio, Reserva, TransporteIda, TransporteVuelta
from apps.locations.models import *
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
            'descripcion' : instance.descripcion,
            'categoria' : instance.categoria,
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



class ClientFormatSerializer(serializers.Serializer):
    pk = serializers.IntegerField()            

    def to_representation(self, value):
        queryset = DetServMov.objects.filter(id_con = value)
        detail_list = []
        
        for x in queryset:
            servicio = Servicio.objects.filter(id=x.id_mov.id.id).first()
            data = {
                'tipo_servicio' : servicio.id_tip.descripcion,
                'fecha_inicio' : x.fecha_inicio,
                'hora_inicio' : x.hora_inicio,
                'fecha_termino' : x.fecha_termino,
                'hora_termino' : x.hora_termino,
                'nombre' : x.id_mov.id.id_reserva.id_cli.id.nombre + ' ' + x.id_mov.id.id_reserva.id_cli.id.ap_paterno + ' ' + x.id_mov.id.id_reserva.id_cli.id.ap_materno,
                'telefono' : x.id_mov.id.id_reserva.id_cli.id.telefono
            } 
            
            if x.id_mov.id.id_tip.id == 1:
                try:
                    transport = TransporteIda.objects.filter(id_trans = x.id_mov.id.id).first()
                    city = Cities.objects.get(id = transport.id_ub_trans.id_ciu)
                    data['tr_ida'] = {
                        'nombre' : transport.id_ub_trans.nombre,
                        'precio' : transport.id_ub_trans.precio,
                        'tipo_ubicacion' : transport.id_ub_trans.id_tip.descripcion,
                        'ciudad' : city.name
                    }
                except Exception as e:
                    print(e)
                    
                try:
                    transport = TransporteVuelta.objects.filter(id_trans = x.id_mov.id.id).first()
                    city = Cities.objects.get(id = transport.id_ub_trans.id_ciu)
                    data['tr_vuelta'] = {
                        'nombre' : transport.id_ub_trans.nombre,
                        'precio' : transport.id_ub_trans.precio,
                        'tipo_ubicacion' : transport.id_ub_trans.id_tip.descripcion,
                        'ciudad' : city.name
                    }
                except Exception as e:
                    print(e)

                print('Servicio de transporte')
            
            if x.id_mov.id.id_tip.id == 2:
                print('SERVICIO TOUR')
                tour = Tour.objects.filter(id=x.id_mov.id.id).first() 
                data['nombre'] = tour.id_ub_trans.nombre
                data['descripcion'] = tour.id_ub_trans.descripcion
                data['precio'] = servicio.precio
                
            detail_list.append(data)


        return {"servicios" : detail_list}