from rest_framework import serializers
from apps.base.models.db_models import Acompaniante, CheckIn, CheckOut, DocIdentidad, EstadoCivil, Genero, Persona, Reserva, CliAcom, Cliente, Vivienda, Servicio, TipoServicio, Movilizacion, Transporte, TransporteIda, TransporteVuelta, DetServMov, DetalleProducto, Inventario, DetalleSala, UbicacionTrans, Tour
from apps.business.models import CuentaBancaria
from apps.locations.models import Cities
from django.db.models import Q

# Configuramos la lectura de nuestras variables de entorno
import environ
env = environ.Env()
environ.Env.read_env(env_file='./.env') 

# Realizar peticiones HTTP
import requests
import json

# Global BASE URL
BASE_URL = env.str('API_PAYMENT')
ACCOUNT_NUMBER = env.int('ACCOUNT_NUMBER')


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

        cant_pasajeros = 0
        if instance.id_tip.id in(1,2):
            detail = DetServMov.objects.get(id_mov__id = instance.id)
            cant_pasajeros = detail.cant_pasajeros
            data['fecha_inicio'] = detail.fecha_inicio
            data['fecha_termino'] = detail.fecha_termino
            data['hora_inicio'] = detail.hora_inicio
            data['hora_termino'] = detail.hora_termino
            data['pasajeros'] = detail.cant_pasajeros
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

        elif instance.id_tip.id == 2: 
            tour = Tour.objects.filter(id=instance.id).first() 
            data['nombre'] = tour.id_ub_trans.nombre
            data['descripcion'] = tour.id_ub_trans.descripcion
            data['precio'] = instance.precio * cant_pasajeros
            print('SERVICIO DE TOUR')

    
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
    id = serializers.IntegerField()
    estado = serializers.CharField(max_length=20)

    def validate_estado(self, value):
        if value not in ('PENDIENTE','COMPLETADO', 'CANCELADO'):
            raise serializers.ValidationError({'estado':'El estado debe ser PENDIENTE, CANCELADO o COMPLETADO.'})
        if value == 'COMPLETADO':
            if not self.context.get('monto'):
                raise serializers.ValidationError({'monto':'Se debe enviar el monto a pagar.'})
            
            checkout = CheckOut.objects.filter(id = self.context['id']).first()
            client = checkout.id_res.id_cli
            account = CuentaBancaria.objects.filter(persona_id = client.id).first()

            global BASE_URL

            headers = {
                'content-type': "application/json",
                'cache-control': "no-cache",
            }

            payload = {
                'cvv' : account.cvv,
                'numeroCuenta' : account.numero_cuenta,
                'titular' : account.nombre_titular,
                'fechaExpiracion' : account.fecha_expiracion,
                'total' : self.context['monto'],
            }
            
            client_response = requests.request("POST", f'{BASE_URL}/account/pago' , data=json.dumps(payload), headers=headers)            
            
            management = {
                'numeroCuenta' : ACCOUNT_NUMBER,
                'monto' : self.context['monto']
            }

            management_response = requests.request("POST", f'{BASE_URL}/account/monto' , data=json.dumps(management), headers=headers)

            if (client_response.status_code and management_response.status_code) != 200:
                raise serializers.ValidationError({'estado':'El pago no se pudo realizar.'})
                
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
    
    def validate_pk(self, value):
        exists = Vivienda.objects.filter(id = value).exists()
        if not exists:
            raise serializers.ValidationError('La vivienda no existe.')
        return value
    
    def get_detail_products(self, pk):
        queryset = DetalleProducto.objects.filter(id_det = pk)
        product_list = []
        for product in queryset:
            data = {
                'id_detalle' : product.id,
                'producto' : {
                    'nombre' : product.id_pro.descripcion,
                    'precio' : product.id_pro.precio,
                    'categoria' : product.id_pro.id_cat.descripcion,
                    'estado' : {
                            'id' : product.id_est.id,
                            'descripcion' : product.id_est.descripcion
                        }
                }
            }
            product_list.append(data)
        return product_list

            
    def get_detail_room(self, queryset):
        room_list = []
        for room in queryset:
            data = {
                    'detalle_sala' : {
                    'id_detalle' : room.id,
                    'imagen' : room.imagen_sala.url if room.imagen_sala.url != '' else '',
                    'tipo_sala' : {
                        'id' : room.id_sal.id,
                        'descripcion' : room.id_sal.descripcion,
                        'detalle_producto' : self.get_detail_products(room.id)                 
                    }
                }
            }
            room_list.append(data)
        return room_list

    def to_representation(self, pk):
        inventory = Inventario.objects.filter(id_viv = pk).first()
        room_queryset = DetalleSala.objects.filter(id_inv = inventory.id)
        return self.get_detail_room(room_queryset)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'

    def validate_cvv(self,value):
        if not value:
            raise serializers.ValidationError({'cvv' : 'Debe enviar un cvv.'})
        return value

    def validate_fecha_expiracion(self,value):
        if not value:
            raise serializers.ValidationError({'fecha_expiracion' : 'Debe enviar una fecha de expiracion.'})
        return value

    def validate_nombre_titular(self,value):
        if not value:
            raise serializers.ValidationError({'nombre_titular' : 'Debe enviar un nombre del titular.'})
        return value

    def validate_numero_cuenta(self,value):
        if not value:
            raise serializers.ValidationError({'numero_cuenta' : 'Debe enviar un numero de cuenta.'})
        if CuentaBancaria.objects.filter(numero_cuenta = value).exists():
            raise serializers.ValidationError({'numero_cuenta' : 'El numero de cuenta ya existe.'})
        return value

