from rest_framework import serializers
from apps.base.models.db_models import Acompaniante, CheckIn, CheckOut, DocIdentidad, EstadoCivil, Genero, Persona, Reserva, CliAcom, Cliente, Vivienda, Servicio, TipoServicio, Movilizacion, Transporte, TransporteIda, TransporteVuelta
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
            print('SERVICIO DE TOUR')
        return data

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
                'nombre' : detail_partners[x].id_aco.id.nombre + ' ' + detail_partners[x].id_aco.id.ap_paterno
            }
            if detail_partners[x].id_aco.id.id_doc.id == 1:
                data['run'] = detail_partners[x].id_aco.id.run
            else:
                data['pasaporte'] = detail_partners[x].id_aco.id.pasaporte

            partner_list.append(data)

        detail_services = Servicio.objects.filter(id_reserva = instance.id)
        services_list = []
        for i in range(len(detail_services)):
            serializer = ServiceBookingSerializer(detail_services[i])
            services_list.append(serializer.data)

        data = {
            'id' : instance.id,
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
            'servicios' : services_list
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





