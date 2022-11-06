from apps.base.models.db_models import Conductor, DetProyecto, Empleado, Reserva, Vivienda
from apps.business.api.general_filters import ServiceFilter
from apps.business.api.services.services_serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from apps.locations.api.general_serializers import *
from rest_framework.decorators import action
from django.db.models import Q

class ServiceViewSet(viewsets.GenericViewSet):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = ServiceSerializer
    filterset_class  = ServiceFilter
    search_fields = ['id']
    ordering_fields = ['id']
    ordering = ['id']

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(estado = 'ACTIVO')
        return self.get_serializer().Meta.model.objects.filter(id = pk, estado = 'ACTIVO').first()

    def list(self, request):
        # with filter
        queryset = self.filter_queryset(self.get_queryset())

        # pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset = Servicio.objects.filter(estado = 'ACTIVO')
        service = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    @action(methods=['GET'],detail=False, url_path = 'search-dates')
    def search_dates(self,request):
        # TODO: pensar bien esta lógica.
        # puede ser mejor enviar la fecha y consultarla directamente si está o no ocupada
        

        # Recibimos el query param de la petición GET
        dwelling_pk = request.query_params.get('pk','')
        passengers = request.query_params.get('passengers','')
        if dwelling_pk == '' or passengers == '':
            return Response({'message':'Se debe enviar pk y passengers.'},status = status.HTTP_400_BAD_REQUEST)

        try:       
            dwelling = Vivienda.objects.get(id = dwelling_pk)
        except:
            return Response(
            {
                'message':'La vivienda enviada no existe.'
            },
            status = status.HTTP_400_BAD_REQUEST)

        queryset = DetProyecto.objects.filter(id_viv = dwelling.id)
        
        drivers = []

        for index in range(len(queryset)):
            if queryset[index].id_emp.id_car.id == 4:
                # Obtenemos la instancia de empleado y luego de conductor
                employee = Empleado.objects.get(id = queryset[index].id_emp.id)
                driver = Conductor.objects.get(id = employee)
                if driver.id_veh.capacidad >= int(passengers):
                    drivers.append(driver)
        
        if len(drivers) == 0:
            return Response(
                {
                    'message':'No hay capacidad en el vehículo.'
                },
                status = status.HTTP_400_BAD_REQUEST)


        # Verificamos las fechas disponibles
        from datetime import datetime
        now = datetime.now()
        
        # Verificamos si tiene capacidad
        dates = DetServMov.objects.filter(
            Q(id_con__in = drivers) & Q(fecha_inicio__gte = now)
        )

        if dates:
            serializer = VerifyDatesSerializer(dates, many = True)
            return Response(
                serializer.data,
                status = status.HTTP_200_OK)
        
        return Response(
            {
                'message':'No se han encontrado fechas registradas para el empleado a cargo del servicio.'
            },
            status = status.HTTP_200_OK)
