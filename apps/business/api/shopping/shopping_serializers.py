from rest_framework import serializers
from apps.base.models.db_models import Reserva, Persona, Vivienda, Cliente, DocIdentidad, EstadoCivil, Genero, Acompaniante, CliAcom, Compra, Servicio, UbicacionTrans, TipoServicio, Movilizacion, Transporte, TransporteIda, TransporteVuelta, Empleado, Conductor, DetProyecto, DetServMov
from django.db.models import Q

class CreateShoppingSerializer(serializers.ModelSerializer):

    # TODO: Se debe añadir a futuro
    # Añadir servicios de tour
    
    acompaniantes = serializers.ListField()
    servicios = serializers.ListField()

    class Meta:
        model = Reserva
        exclude = ('estado','creacion','actualizacion')

    def search_driver(self,dwelling_id, date):
        # Asignamos un conductor al servicio
        queryset = DetProyecto.objects.filter(id_viv = dwelling_id)
        response = None
        drivers = []

        for index in range(len(queryset)):
            if queryset[index].id_emp.id_car.id == 4:
                # Obtenemos la instancia de empleado y luego de conductor
                employee = Empleado.objects.get(id = queryset[index].id_emp.id)
                driver = Conductor.objects.get(id = employee)
                drivers.append(driver)
        
        # Verificamos las fechas disponibles
        
        details = DetServMov.objects.filter(
            Q(id_con__in = drivers) & (Q(fecha_inicio__gte = date) | Q(fecha_termino__gte = date))
        )

        if len(drivers) > len(details):
            available = drivers
            if len(details) != 0:
            # Elimino los conductores
                for detail in details:
                    available.remove(detail.id_con)
            import random
            index = random.randint(0, len(available))
            response = available[index]
        return response

    def find_acompaniante(self,data):
        flag = False
        persona = None
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

    def validate_servicios(self, values):
        if len(values) > 0:
            try:
                for index in range(len(values)):
                    if values[index]["id_tipo"] == 1:
                        values[index]["id_ubicacion"]
                        values[index]["id_transporte"]
                    elif values[index]["id_tipo"] == 2:
                        pass
            except:
                raise serializers.ValidationError('¡Servicio en mal formato!')
        return values

    def create(self,validated_data):
        acompaniantes = validated_data['acompaniantes'] 
        servicios = validated_data['servicios']


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

        # Generamos la compra
        compra = Compra(id_cliente = cliente, monto_final = 0, id_reserva = reserva)
        compra.save()

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
            
        if len(servicios) > 0:
            # Agregamos los servicios
            for index in range(len(servicios)):
                if servicios[index]["id_tipo"] == 1:
                    ubicacion = UbicacionTrans.objects.get(id = servicios[index]["id_ubicacion"])
                    tipo_servicio = TipoServicio.objects.get(id = servicios[index]["id_tipo"])
                    servicio = Servicio(id_tip = tipo_servicio, id_reserva = reserva, precio = ubicacion.precio)
                    servicio.save()
                    # Movilizacion
                    movilizacion = Movilizacion(id = servicio)
                    movilizacion.save()
                    # Transporte
                    transporte = Transporte(id = movilizacion)
                    transporte.save()
                    # es de ida o de vuelta?
                    # Transporte ida Tranporte Vuelta
                    if servicios[index]["id_transporte"] == 1:
                        tipo_transporte = TransporteIda(id_trans = transporte, id_ub_trans = ubicacion)  
                        driver = self.search_driver(vivienda.id, reserva.fecha_inicio)    
                        date = reserva.fecha_inicio
                    else:
                        tipo_transporte = TransporteVuelta(id_trans = transporte, id_ub_trans = ubicacion)
                        driver = self.search_driver(vivienda.id, reserva.fecha_termino)
                        date = reserva.fecha_termino
                    tipo_transporte.save()

                    if driver:
                        print('Existe el conductor')
                        detail_driver = DetServMov(id_con = driver, id_mov = movilizacion, fecha_inicio = date, fecha_termino = date, 
                        hora_inicio = '10:00', hora_termino = '11:00', cant_pasajeros = 0)
                        detail_driver.save()   
                    else:
                        print('No existe conductor')
                if servicios[index]["id_tipo"] == 2:
                    pass
                
        return True


# Le especifico el formato como quiero que se envien los datos
# TODO: Falta implementar lógica para tours
class ValidateServiceSerializer(serializers.Serializer):
    id_tipo = serializers.IntegerField()
    id_ubicacion = serializers.IntegerField(required=False)
    id_transporte = serializers.IntegerField(required=False)
class ServicePaymentSerializer(serializers.Serializer):
    # Defino que puede recibir muchos servicios
    services = ValidateServiceSerializer(many=True,  read_only=True)


    def validate_services(self, values):
        print(values)
        return values

    def create(self, validated_data):
        return True