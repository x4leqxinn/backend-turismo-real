from apps.locations.api.filters import CityFilter
from apps.locations.api.general_serializers import CitySerializers
from apps.locations.models import Cities
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class CityViewSet(viewsets.GenericViewSet):
    serializer_class = CitySerializers
    filterset_class  = CityFilter
    search_fields = ['id']
    ordering_fields = ['id']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ["create"]:
            return None
        elif self.action in ["list"]:
            return CitySerializers
        return self.serializer_class


    def get_queryset(self):
        return Cities.objects.all()

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
        queryset = Cities.objects.all()
        country = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializers(country)
        return Response(serializer.data)

    @action(methods=['GET'],detail=False, url_path = 'find-by-state')
    def find_by_state(self,request):
        # Recibimos el query param de la petición GET
        state_pk = request.query_params.get('pk','')
        if state_pk == '':
            return Response({'message':'Se deber enviar un id.'},status = status.HTTP_400_BAD_REQUEST)

        queryset = Cities.objects.filter(state_id = state_pk)
        
        if queryset:
            serializer = CitySerializers(queryset, many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        
        return Response(
            {
                'message':'No se han encontrado estados para el país con id '  + state_pk + '.'
            },
            status = status.HTTP_400_BAD_REQUEST)
