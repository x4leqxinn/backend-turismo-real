from apps.locations.api.filters import CountryStateFilter
from apps.locations.api.general_serializers import CountryStateSerializers
from apps.locations.models import States
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status

class StateViewSet(viewsets.GenericViewSet):
    serializer_class = CountryStateSerializers
    filterset_class  = CountryStateFilter
    search_fields = ['id']
    ordering_fields = ['id']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ["create"]:
            return None
        elif self.action in ["list"]:
            return CountryStateSerializers
        return self.serializer_class


    def get_queryset(self):
        return States.objects.all()

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

    def retrieve(self, request, pk=None):
        queryset = States.objects.all()
        state = get_object_or_404(queryset, pk=pk)
        serializer = CountryStateSerializers(state)
        return Response(serializer.data)


    @action(methods=['GET'],detail=False, url_path = 'find-by-country')
    def find_by_country(self,request):
        # Recibimos el query param de la petición GET
        country_pk = request.query_params.get('pk','')
        if country_pk == '':
            return Response({'message':'Se deber enviar un id.'},status = status.HTTP_400_BAD_REQUEST)

        queryset = States.objects.filter(country_id = country_pk)
        
        if queryset:
            serializer = CountryStateSerializers(queryset, many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        
        return Response(
            {
                'message':'No se han encontrado estados para el país con id '  + country_pk + '.'
            },
            status = status.HTTP_400_BAD_REQUEST)