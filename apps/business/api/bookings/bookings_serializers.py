from rest_framework import serializers
from apps.base.models.db_models import Acompaniante, CheckIn, CheckOut, DocIdentidad, EstadoCivil, Genero, Persona, Reserva, CliAcom, Cliente, Vivienda
from apps.locations.models import Cities
from django.db.models import Q

class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')

    def to_representation(self, instance):
        city = Cities.objects.get(id = instance.id_viv.id_ciu)
        return {
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
            }
        }

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
            data['check_out'] = checkout.estado_checkout
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


class BookingCreateSerializer(serializers.ModelSerializer):

    # TODO: Se debe añadir a futuro.
    #  agregar servicios iniciales al momento de hacer la reserva 
    acompaniantes = serializers.ListField()

    class Meta:
        model = Reserva
        exclude = ('estado','creacion','actualizacion')

    def find_acompaniante(self,data):
        flag = False
        persona = None
        print(data)
        if data["id_doc"] == 1: 
            try:
                persona = Persona.objects.get(run = data["run"])
                flag = True
            except:
                pass
        else:
            try:
                persona = Persona.objects.get(pasaporte = data["pasaporte"])
                flag = True
            except:
                pass
        return flag, persona

    def validate_acompaniantes(self, values):
        if len(values) > 0:
            # Verificamos que tenga el formato correcto
            try:
                for index in range(len(values)):
                    values[index]["run"]
                    values[index]["dv"]
                    values[index]["pasaporte"]
                    values[index]["nombre"]
                    values[index]["snombre"]
                    values[index]["ap_paterno"]
                    values[index]["ap_materno"]
                    values[index]["fecha_nacimiento"]
                    values[index]["telefono"]
                    values[index]["num_calle"]
                    values[index]["calle"]
                    values[index]["id_ciu"]
                    values[index]["id_est"]
                    values[index]["id_pai"]
                    values[index]["id_doc"]
                    values[index]["id_est1"]
                    values[index]["id_gen"]
            except:
                raise serializers.ValidationError('¡Acompañante en mal formato!')

        return values

    def create(self,validated_data):
        acompaniantes = validated_data['acompaniantes'] 


        vivienda = Vivienda.objects.get(id = validated_data['id_viv'].id)
        cliente = Cliente.objects.get(id = validated_data['id_cli'].id)

        # Reserva
        reserva = Reserva(id_cli = cliente, 
        id_viv = vivienda, fecha_inicio = validated_data['fecha_inicio'],
        fecha_termino = validated_data['fecha_termino'], abono = validated_data['abono'],
        monto_pagado = validated_data['monto_pagado'], total_pago = validated_data['total_pago'],
        cant_acompaniante = validated_data['cant_acompaniante'],
        cant_total = validated_data['cant_total'])
        reserva.save()

        if len(acompaniantes) > 0:
            # Agregamos los acompañantes al sistema
            for index in range(len(acompaniantes)):  

                flag, persona = self.find_acompaniante(acompaniantes[index])

                docIdentidad = DocIdentidad.objects.get(id = acompaniantes[index]["id_doc"] )
                estadoCivil = EstadoCivil.objects.get(id = acompaniantes[index]["id_est1"])
                genero = Genero.objects.get(id = acompaniantes[index]["id_gen"])

                if(flag == False):
                    print('Validar')
                    persona = Persona()

                persona.run = acompaniantes[index]["run"]
                persona.dv = acompaniantes[index]["dv"]
                persona.pasaporte = acompaniantes[index]["pasaporte"]
                persona.nombre = acompaniantes[index]["nombre"]
                persona.snombre = acompaniantes[index]["snombre"]
                persona.ap_paterno = acompaniantes[index]["ap_paterno"]
                persona.ap_materno = acompaniantes[index]["ap_materno"]
                persona.fecha_nacimiento = acompaniantes[index]["fecha_nacimiento"]
                persona.telefono = acompaniantes[index]["telefono"]
                persona.num_calle = acompaniantes[index]["num_calle"]
                persona.calle = acompaniantes[index]["calle"]
                persona.id_ciu = acompaniantes[index]["id_ciu"]
                persona.id_est = acompaniantes[index]["id_est"]
                persona.id_pai = acompaniantes[index]["id_pai"]
                persona.id_doc = docIdentidad
                persona.id_est1 = estadoCivil
                persona.id_gen = genero                
                persona.save()
                
                acompaniante = Acompaniante(id = persona)
                acompaniante.save()

                # Generar detalle
                detalle = CliAcom(id_cli = cliente, id_aco = acompaniante, id_res = reserva)
                detalle.save()

        return True






