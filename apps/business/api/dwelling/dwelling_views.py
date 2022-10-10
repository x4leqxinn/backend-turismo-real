from apps.business.api.general_filters import DwellingFilter
from apps.business.api.dwelling.dwelling_serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from apps.base.stored_procedures import genericDelete
from apps.locations.models import Countries
from db_routers.permissions.db_connection import oracle_connection
from rest_framework.decorators import action
from apps.locations.api.general_serializers import *

class DwellingViewSet(viewsets.GenericViewSet):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = DwellingSerializer
    filterset_class  = DwellingFilter
    search_fields = ['id','id_dis__descripcion','id_ciu__nombre','id_ciu__id_est__nombre','id_ciu__id_est__id_pai__nombre']
    ordering_fields = ['gas','luz','agua','internet','capacidad','abono_base','valor_noche','estrellas','id']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ["create"]:
            return None
        elif self.action in ["list"]:
            return DwellingSerializer
        return self.serializer_class

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
        queryset = Vivienda.objects.filter(estado = 'ACTIVO')
        dwelling = get_object_or_404(queryset, pk=pk)
        serializer = DwellingSerializer(dwelling)
        return Response(serializer.data)

    # TODO: Optimizar consultas
    @action(methods=['GET'],detail=False, url_path = 'search-country')
    def search_country(self,request):
        # Recibimos el query param de la petición GET
        country_name = request.query_params.get('country_name','')
        country = Countries.objects.filter(name__icontains = country_name).first()
        if country:
            queryset = Vivienda.objects.filter(estado = 'ACTIVO', id_pai = country.id)
            serializer = DwellingSerializer(queryset, many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(
            {
                'message':'No se han encontrado coincidencias con el término '  + country_name + '.'
            },
            status = status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'],detail=False, url_path = 'search-state')
    def search_state(self,request):
        # Recibimos el query param de la petición GET
        state_name = request.query_params.get('state_name','')
        state = States.objects.filter(name__icontains = state_name).first()
        if state:
            queryset = Vivienda.objects.filter(estado = 'ACTIVO', id_est = state.id)
            serializer = DwellingSerializer(queryset, many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(
            {
                'message':'No se han encontrado coincidencias con el término '  + state_name + '.'
            },
            status = status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'],detail=False, url_path = 'search-city')
    def search_city(self,request):
        # Recibimos el query param de la petición GET
        city_name = request.query_params.get('city_name','')
        queryset = Cities.objects.filter(name__icontains = city_name)
        cities = []
        for city in queryset:
            print(city.id)
            cities.append(city.id)

    
        if len(cities) > 0:
            queryset = Vivienda.objects.filter(estado = 'ACTIVO', id_ciu__in = cities)
            serializer = DwellingSerializer(queryset, many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(
            {
                'message':'No se han encontrado coincidencias con el término '  + city_name + '.'
            },
            status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        if self.get_queryset(pk):
            dwelling_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if dwelling_serializer.is_valid():
                dwelling_serializer.save()
                return Response({'message' : '¡Vivienda Modificada con éxito!'}, status = status.HTTP_200_OK)
            return Response(dwelling_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        dwelling = self.get_queryset().filter(id = pk).first()
        if dwelling and genericDelete(oracle_connection(1),pk,'VIVIENDA') == 1: 
            return Response({'message':'Vivienda eliminada correctamente.'}, status = status.HTTP_200_OK)
        return Response({'Error' :  '¡No existe una vivienda con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
