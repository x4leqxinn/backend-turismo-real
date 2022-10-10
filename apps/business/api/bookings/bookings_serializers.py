from pyexpat import model
from rest_framework import serializers
from apps.base.models.db_models import Acompaniante, DocIdentidad, EstadoCivil, Genero, Persona, Reserva, CliAcom, Cliente, Vivienda
from apps.locations.models import Cities


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')

    def to_representation(self, instance):
        city = Cities.objects.get(id = instance.id_viv.id_ciu)
        return {
            'id' : instance.id,
            # TODO: Hay que serializar el modelo persona
            'cliente' : {
                #'id' : instance.id_cli.id
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
            }
        }

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

    acompaniantes = serializers.ListField()

    class Meta:
        model = Reserva
        exclude = ('estado','creacion','actualizacion')

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

        print('ojo' , validated_data['id_viv'])

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

                docIdentidad = DocIdentidad.objects.get(id = acompaniantes[index]["id_doc"] )
                estadoCivil = EstadoCivil.objects.get(id = acompaniantes[index]["id_est1"])
                genero = Genero.objects.get(id = acompaniantes[index]["id_gen"])
                persona = Persona(
                    run = acompaniantes[index]["run"],
                    dv = acompaniantes[index]["dv"],
                    pasaporte = acompaniantes[index]["pasaporte"],
                    nombre = acompaniantes[index]["nombre"],
                    snombre = acompaniantes[index]["snombre"],
                    ap_paterno = acompaniantes[index]["ap_paterno"],
                    ap_materno = acompaniantes[index]["ap_materno"],
                    fecha_nacimiento = acompaniantes[index]["fecha_nacimiento"],
                    telefono = acompaniantes[index]["telefono"],
                    num_calle = acompaniantes[index]["num_calle"],
                    calle = acompaniantes[index]["calle"],
                    id_ciu = acompaniantes[index]["id_ciu"],
                    id_est = acompaniantes[index]["id_est"],
                    id_pai = acompaniantes[index]["id_pai"],
                    id_doc = docIdentidad,
                    id_est1 = estadoCivil,
                    id_gen = genero
                )
                persona.save()
                
                acompaniante = Acompaniante(id = persona)
                acompaniante.save()

                # Generar detalle
                detalle = CliAcom(id_cli = cliente, id_aco = acompaniante, id_res = reserva)
                detalle.save()

        return True
