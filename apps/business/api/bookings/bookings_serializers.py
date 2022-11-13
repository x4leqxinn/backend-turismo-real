from rest_framework import serializers
from apps.base.models.db_models import Acompaniante, CheckIn, CheckOut, DocIdentidad, EstadoCivil, Genero, Persona, Reserva, CliAcom, Cliente, Vivienda, Servicio, TipoServicio, Movilizacion, Transporte, TransporteIda, TransporteVuelta, DetServMov, DetalleProducto, Inventario, DetalleSala
from apps.locations.models import Cities
from django.db.models import Q


#
class ServiceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        exclude = ('creacion','actualizacion','estado')

    def to_representation(self, instance):
        data = {
            'id' : instance.id,
            'tipo_servicio' : instance.id_tip.descripcion,
            'precio' : instance.precio
        }

        driver = False

        if instance.id_tip.id == 1:
            transporte = None
            try:
                transporte = TransporteIda.objects.get(id_trans = instance.id)
                data['tipo_tranporte'] = 'TRANPORTE DE IDA'
            except:
                pass

            try: 
                transporte = TransporteVuelta.objects.get(id_trans = instance.id)
                data['tipo_tranporte'] = 'TRANPORTE DE VUELTA'
            except:
                pass

            data['nombre'] = transporte.id_ub_trans.nombre 
            data['descripcion'] = transporte.id_ub_trans.id_tip.descripcion
            data['precio'] = transporte.id_ub_trans.precio 
            driver = True

        elif instance.id_tip.id == 2:
            print('SERVICIO DE TOUR')

        if driver:
            detail = DetServMov.objects.get(id_mov__id = transporte.id_trans.id.id.id)
            driver = {
                'run' : detail.id_con.id.id.run,
                'nombre' : detail.id_con.id.id.nombre + ' ' + detail.id_con.id.id.ap_paterno + ' ' + detail.id_con.id.id.ap_materno,
                'telefono' : detail.id_con.id.id.telefono,
                'vehiculo' : {
                    'patente' : detail.id_con.id_veh.patente,
                    'modelo' : detail.id_con.id_veh.id_mod.nombre,
                    'marca' : detail.id_con.id_veh.id_mar.nombre,
                    'color' : detail.id_con.id_veh.id_col.nombre
                }
            }
            data['conductor'] = driver
            # detalle serv movilizacion     
        return data

class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = ('id','creacion','id_viv')

    def to_representation(self, instance):
        data = {
            'id' : instance.id,
            'fecha_creacion' : instance.creacion.now().date(),
            'departamento' : instance.id_viv.nombre,
        }

        try:
            checkin = CheckIn.objects.get(id_res = instance.id)
            data['check_in'] = checkin.fecha_llegada
            data['estado_checkin'] = checkin.estado_checkin
        except Exception as e:
            data['check_in'] = 'N/A'
            data['estado_checkin'] = 'N/A'

        try:
            checkout = CheckOut.objects.get(id_res = instance.id)
            data['check_out'] = checkout.fecha_salida
            data['estado_checkout'] = checkout.estado_checkout
        except Exception as e:
            data['check_out'] = 'N/A'
            data['estado_checkout'] = 'N/A'
        
        return data

class BookingDatesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reserva
        fields = ('fecha_inicio','fecha_termino')

    def to_representation(self, instance):
        return {
            'start' : instance.fecha_inicio,
            'end' : instance.fecha_termino,
        }

class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')


    def to_representation(self, instance):
        city = Cities.objects.get(id = instance.id_viv.id_ciu)
        detail_partners = CliAcom.objects.filter(id_res = instance.id)
        partner_list = []
        for x in range(len(detail_partners)):
            data = {
                'id' : detail_partners[x].id_aco.id.id,
                'nombre' : detail_partners[x].id_aco.id.nombre + ' ' + detail_partners[x].id_aco.id.ap_paterno,
                'dni' : detail_partners[x].id_cli.id.run if detail_partners[x].id_cli.id.id_doc.id == 1 else detail_partners[x].id_cli.id.pasaporte
            }
            partner_list.append(data)

        detail_services = Servicio.objects.filter(id_reserva = instance.id)
        services_list = []
        for i in range(len(detail_services)):
            serializer = ServiceBookingSerializer(detail_services[i])
            services_list.append(serializer.data)

        data = {
            'id' : instance.id,
            'cliente' : {
                'nombre' : instance.id_cli.id.nombre + ' ' + instance.id_cli.id.ap_paterno + ' ' + instance.id_cli.id.ap_materno,
                'telefono' : instance.id_cli.id.telefono,
                'dni' : instance.id_cli.id.run if instance.id_cli.id.id_doc.id == 1 else instance.id_cli.id.pasaporte
            },
            'vivienda' : {
                'id' : instance.id_viv.id,
                'tipo_vivienda' : {
                    'id' : instance.id_viv.id_tip.id,
                    'descripcion' : instance.id_viv.id_tip.descripcion
                },
                'nombre' : instance.id_viv.nombre,
                'descripcion' : instance.id_viv.descripcion,
                'valor_noche' : instance.id_viv.valor_noche,
                'direccion' : instance.id_viv.direccion,
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
            },
            'fecha_inicio' : instance.fecha_inicio,
            'fecha_termino' : instance.fecha_termino,
            'abono' : instance.abono,
            'monto_pagado' : instance.monto_pagado,
            'total_pago' : instance.total_pago,
            'cant_personas' : instance.cant_total,
            'acompaniantes' : partner_list,
            'servicios' : services_list,
        }

        try:
            checkin = CheckIn.objects.get(id_res = instance.id)
            data['checkin_pk'] = checkin.id 
            data['check_in'] = checkin.fecha_llegada
            data['estado_checkin'] = checkin.estado_checkin
        except Exception as e:
            data['check_in'] = 'N/A'
            data['estado_checkin'] = 'N/A'
        try:
            checkout = CheckOut.objects.get(id_res = instance.id)
            data['checkout_pk'] = checkout.id
            data['check_out'] = checkout.fecha_salida
            data['estado_checkout'] = checkout.estado_checkout
            data['multa'] = checkout.total_multa if checkout.total_multa else 0
        except Exception as e:
            data['check_out'] = 'N/A'
            data['estado_checkout'] = 'N/A'
        

        return data



class CheckinSerializer(serializers.Serializer):
    estado = serializers.CharField(max_length=20)

    def validate_estado(self, value):
        if value not in ('PENDIENTE','PAGADO','CANCELADO'):
            raise serializers.ValidationError({'estado':'El estado debe ser PENDIENTE, PAGADO o CANCELADO.'})
        return value

class CheckoutSerializer(serializers.Serializer):
    estado = serializers.CharField(max_length=20)

    def validate_estado(self, value):
        if value not in ('PENDIENTE','COMPLETADO', 'CANCELADO'):
            raise serializers.ValidationError({'estado':'El estado debe ser PENDIENTE, CANCELADO o COMPLETADO.'})
        return value


class ValidateStateProductSerializer(serializers.Serializer):
    # detail id
    pk = serializers.IntegerField()
    state_id = serializers.IntegerField()

    def validate_pk(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError({'pk' : 'Debe ingresar un pk.'})
        exists = DetalleProducto.objects.filter(id = value).exists()
        if not exists:
            raise serializers.ValidationError({'pk' : 'No se pudo actualizar.'})
        return value

    def validate_state_id(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError({'state_id' : 'Debe ingresar un estado id.'})
        if value not in (1,2,3,4,5,6):
            raise serializers.ValidationError({'state_id':'El estado id deber estar entre 1 y 6.'})
        return value

class UpdateCheckListProductSerializer(serializers.Serializer):
    check_list = ValidateStateProductSerializer(many=True)

    def update(self, instances, validated_data):
        for key in instances['check_list']:
            DetalleProducto.objects.filter(id = key['pk']).update(id_est = key['state_id'])
        return validated_data

class ListCheckListProductSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    serializer_data = {}
    serializer_list = []
    
    def validate_pk(self, value):
        exists = Vivienda.objects.filter(id = value).exists()
        if not exists:
            raise serializers.ValidationError('La vivienda no existe.')
        return value
    
    def get_detail_product(self,queryset):
        for product in queryset:
            self.add_hash('detalle_producto' , {
                'id_detalle' : product.id,
                'producto' : {
                    'nombre' : product.id_pro.descripcion,
                    'precio' : product.id_pro.precio,
                    'categoria' : product.id_pro.id_cat.descripcion,
                },
                'estado' : {
                    'id' : product.id_est.id,
                    'descripcion' : product.id_est.descripcion
                }
            })

            self.serializer_list.append(self.serializer_data)
            
    def get_detail_room(self, queryset):
        for room in queryset:
            self.add_hash('detalle_sala', {
                'id_detalle' : room.id,
                'imagen' : room.imagen_sala.url if room.imagen_sala.url != '' else '',
                'tipo_sala' : {
                    'id' : room.id_sal.id,
                    'descripcion' : room.id_sal.descripcion                    
                }
            })

            self.get_detail_product(DetalleProducto.objects.filter(id_det = room.id))

            
    def add_hash(self, key, value):
        self.serializer_data[key] = value

    def to_representation(self, pk):
        inventory = Inventario.objects.filter(id_viv = pk).first()
        room_queryset = DetalleSala.objects.filter(id_inv = inventory.id)
        self.add_hash('pk',pk)
        self.get_detail_room(room_queryset)
        print(len(self.serializer_list))
        #print(self.serializer_list[0])
        
        return self.serializer_list[0]
