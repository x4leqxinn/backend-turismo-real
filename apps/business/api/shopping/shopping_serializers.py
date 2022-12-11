from rest_framework import serializers
from apps.base.models.db_models import Reserva, Persona, Vivienda, Cliente, DocIdentidad, EstadoCivil, Genero, Acompaniante, CliAcom, Compra, Servicio, UbicacionTrans, TipoServicio, Movilizacion, Transporte, TransporteIda, TransporteVuelta, Empleado, Conductor, DetProyecto, DetServMov, Recepcionista, CheckIn, CheckOut, Tour
from django.db.models import Q
from core.templates.views import prefix_decorator


def find_acompaniante(data):
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
class CreateShoppingSerializer(serializers.ModelSerializer):

    
    acompaniantes = serializers.ListField()
    servicios = serializers.ListField()

    class Meta:
        model = Reserva
        exclude = ('estado','creacion','actualizacion')

    # Sólo un recepcionista estará asociado a una vivienda
    def search_receptionist(self, dwelling_id):
        queryset =  DetProyecto.objects.filter(id_viv = dwelling_id)
        response = None

        for index in range(len(queryset)):
            if queryset[index].id_emp.id_car.id == 3:
                # Obtenemos la instancia de empleado y luego de recepcionista
                employee = Empleado.objects.get(id = queryset[index].id_emp.id)
                receptionist = Recepcionista.objects.get(id = employee)
                response = receptionist
                break
        return response

    def search_driver(self,dwelling_id, date):
        # Asignamos un conductor al servicio
        queryset = DetProyecto.objects.filter(id_viv = dwelling_id, estado = 'ACTIVO')
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
            Q(id_con__in = drivers) & Q(estado = 'ACTIVO') & (Q(fecha_inicio = date) | Q(fecha_termino = date))
        )


        if len(drivers) > len(details):
            available = drivers
            if len(details) != 0:
            # Elimino los conductores
                for detail in details:
                    available.remove(detail.id_con)
            import random

            index = random.randint(0, len(available) - 1)
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
                        values[index]["id_ubicacion"]
                        values[index]["cant_pasajeros"]
                        values[index]["fecha"]
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
        compra = Compra(id_cliente = cliente, monto_final = reserva.total_pago, id_reserva = reserva)
        compra.save()

        @prefix_decorator(email_type='booking',page=1,booking=reserva)
        def extras():
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
                        ubicacion = UbicacionTrans.objects.get(id = servicios[index]["id_ubicacion"])
                        tipo_servicio = TipoServicio.objects.get(id = servicios[index]["id_tipo"])
                        servicio = Servicio(id_tip = tipo_servicio, id_reserva = reserva, precio = ubicacion.precio * servicios[index]["cant_pasajeros"])
                        servicio.save()
                        # Movilizacion
                        movilizacion = Movilizacion(id = servicio)
                        movilizacion.save()
                        # Tour
                        tour = Tour(id = movilizacion, id_ub_trans = ubicacion)
                        tour.save()

                        from datetime import datetime
                        # Buscamos el conductor
                        driver = self.search_driver(vivienda.id, datetime.strptime(servicios[index]["fecha"],'%d-%m-%Y'))
                        date = reserva.fecha_termino
                        
                        if driver:
                            print('Existe el conductor')
                            date = datetime.strptime(servicios[index]["fecha"],'%d-%m-%Y')
                            detail_driver = DetServMov(id_con = driver, id_mov = movilizacion, 
                            fecha_inicio = date, fecha_termino = date, 
                            hora_inicio = '10:00', hora_termino = '20:00', 
                            cant_pasajeros = servicios[index]["cant_pasajeros"])
                            detail_driver.save()
                        else:
                            print('No existe conductor')
                    
                    # Sumamos al valor total de la compra
                    compra.monto_final = compra.monto_final + servicio.precio
                    compra.save()

            recepcionist = self.search_receptionist(vivienda.id)
            if recepcionist:
                # Crear Check In
                CheckIn.objects.create(fecha_llegada = reserva.fecha_inicio, hora_llegada = '10:00',
                firma = None, estado_checkin = 'PENDIENTE', id_res = reserva, id_rec = recepcionist)

                CheckOut.objects.create(fecha_salida = reserva.fecha_termino, hora_salida = '10:00',
                estado_checkout = 'PENDIENTE', total_multa = None, id_rec = recepcionist, id_res = reserva)
                print('Check In y Check out Creados!')
            else:
                print('No existe recepcionista')
        
        # Generamos un mail
        extras()

        return True


def search_driver(dwelling_id, date):
    # Asignamos un conductor al servicio
    queryset = DetProyecto.objects.filter(id_viv = dwelling_id, estado = 'ACTIVO')
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
        Q(id_con__in = drivers) & Q(estado = 'ACTIVO') & (Q(fecha_inicio = date) | Q(fecha_termino = date))
    )


    if len(drivers) > len(details):
        available = drivers
        if len(details) != 0:
        # Elimino los conductores
            for detail in details:
                available.remove(detail.id_con)
        import random

        index = random.randint(0, len(available) - 1)
        response = available[index]
    return response

class ValidateServiceSerializer(serializers.Serializer):
    id_tipo = serializers.IntegerField(required=True)
    id_ubicacion = serializers.IntegerField(required=True)
    id_transporte = serializers.IntegerField(required=False)
    cant_pasajeros = serializers.IntegerField(required=False)
    fecha = serializers.DateField(required=False)
class ServicePaymentSerializer(serializers.Serializer):
    id_reserva = serializers.IntegerField(required=True)
    # Defino que puede recibir muchos servicios
    services = ValidateServiceSerializer(many=True)

    def validate_id_reserva(self,value):
        exists =  Reserva.objects.filter(id=value)
        if not exists:
            raise serializers.ValidationError({'id_reserva':'¡No existe la reserva!'})
        return exists.first()

    def validate_services(self, services):
        for service in services:
            # Transporte
            if service.get('id_tipo') == 1 and (not service.get('id_transporte')):                
                raise serializers.ValidationError({'id_transporte':'¡Se debe enviar id transporte en servicio de transporte!'})
            if service.get('id_tipo') == 1 and service.get('id_transporte') == 1:
                raise serializers.ValidationError({'id_transporte':'¡No se puede contratar un servicio de ida!'})
            if service.get('id_tipo') == 1:
                list_services = Servicio.objects.filter(id_reserva=self.context['id_reserva'],id_tip=1)
                for x in list_services:
                    if TransporteVuelta.objects.filter(id_trans=x.id).exists():
                        raise serializers.ValidationError({'id_transporte':'¡Ya posees un servicio de vuelta vigente!'})
            # Tour
            if service.get('id_tipo') == 2 and ((not service.get('cant_pasajeros')) or (not service.get('fecha'))):
                raise serializers.ValidationError({'tour':'Asegúrese de enviar la cant de pasajeros y la fecha.'})
        return services

    def create(self, validated_data):
        servicios = validated_data['services']
        reserva = validated_data['id_reserva']
        compra = Compra.objects.get(id_reserva=reserva)
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
                        driver = search_driver(reserva.id_viv.id, reserva.fecha_inicio)    
                        date = reserva.fecha_inicio
                    else:
                        tipo_transporte = TransporteVuelta(id_trans = transporte, id_ub_trans = ubicacion)
                        driver = search_driver(reserva.id_viv.id, reserva.fecha_termino)
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
                    ubicacion = UbicacionTrans.objects.get(id = servicios[index]["id_ubicacion"])
                    tipo_servicio = TipoServicio.objects.get(id = servicios[index]["id_tipo"])
                    servicio = Servicio(id_tip = tipo_servicio, id_reserva = reserva, precio = ubicacion.precio * servicios[index]["cant_pasajeros"])
                    servicio.save()
                    # Movilizacion
                    movilizacion = Movilizacion(id = servicio)
                    movilizacion.save()
                    # Tour
                    tour = Tour(id = movilizacion, id_ub_trans = ubicacion)
                    tour.save()

                    # Buscamos el conductor
                    driver = search_driver(reserva.id_viv.id, servicios[index]["fecha"])
                    date = reserva.fecha_termino
                    
                    if driver:
                        print('Existe el conductor')
                        date = servicios[index]["fecha"]
                        detail_driver = DetServMov(id_con = driver, id_mov = movilizacion, 
                        fecha_inicio = date, fecha_termino = date, 
                        hora_inicio = '10:00', hora_termino = '20:00', 
                        cant_pasajeros = servicios[index]["cant_pasajeros"])
                        detail_driver.save()
                    else:
                        print('No existe conductor')
                
                # Sumamos al valor total de la compra
                compra.monto_final = compra.monto_final + servicio.precio
                compra.save()
        return True



class CompanionFormatted(serializers.ModelSerializer):
    class Meta: 
        model = Persona
        fields = '__all__'


class AddCompanionSerializer(serializers.Serializer):
    id_reserva = serializers.IntegerField(required=True)
    companions = CompanionFormatted(many=True)

    def validate_id_reserva(self,value):
        exists =  Reserva.objects.filter(id=value)
        if not exists:
            raise serializers.ValidationError({'id_reserva':'¡No existe la reserva!'})
        return exists.first()

    def validate_companions(self,companions):
        for companion in companions:
            # Cédula de identidad
            if companion.get('id_doc').id == 1 and not (companion.get('run') and companion.get('dv')):
                raise serializers.ValidationError({'id_doc':'Debe enviar un rut y un dv'})
            if companion.get('id_doc').id == 2 and not companion.get('pasaporte'):
                raise serializers.ValidationError({'id_doc':'Debe enviar un pasaporte'})
            if companion.get('id_doc').id == 2:
                companion['run'], companion['dv'] = None, None
            companion['pasaporte'] = companion.get('pasaporte') if companion.get('id_doc').id == 2 else None
        return companions

    def validate(self,data):
        reserva, dwelling = data['id_reserva'], data['id_reserva'].id_viv
        # current date
        from datetime import date   
        time = date.today()
        # Validamos que sólo pueda agregar acompañantes 1 día antes de su llegada
        if(time == reserva.fecha_inicio):
            raise serializers.ValidationError({'fecha':'¡El usuario sólo puede agregar acompañantes antes de su llegada!'})
        # Validar cantidad de acompañantes en la reserva
        count, available = len(data['companions']), (dwelling.capacidad - reserva.cant_total)
        if count > available:
            message = 'no hay espacios disponibles.' if available == 0 else 'sólo quedan {available} espacios disponibles.'
            message = 'sólo queda 1 espacio disponible' if available == 1 else message
            msg = 'acompañante' if count == 1 else 'acompañantes'
            raise serializers.ValidationError({'capacidad':f'¡Se intentó añadir {count} {msg} y ' +  message})
        data['client'] = reserva.id_cli
        return data

    def create(self,validated_data):
        acompaniantes = validated_data['companions']
        count = len(acompaniantes)
        if count > 0:
            # Agregamos los acompañantes al sistema
            for index in range(len(acompaniantes)):  

                flag, persona = find_acompaniante(acompaniantes[index])

                docIdentidad = DocIdentidad.objects.get(id = acompaniantes[index]["id_doc"].id )
                estadoCivil = EstadoCivil.objects.get(id = acompaniantes[index]["id_est1"].id)
                genero = Genero.objects.get(id = acompaniantes[index]["id_gen"].id)

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

                booking = validated_data['id_reserva']

                # Generar detalle
                detalle = CliAcom(id_cli = validated_data['client'], id_aco = acompaniante, id_res = booking)
                detalle.save()

                # Actualizo la reserva
                booking.cant_acompaniante = booking.cant_acompaniante + count 
                booking.cant_total = booking.cant_total + count
                booking.save()
        return True
