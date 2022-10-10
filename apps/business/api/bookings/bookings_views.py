from apps.base.models.db_models import Reserva
from apps.business.api.general_filters import BookingFilter
from apps.business.api.bookings.bookings_serializers import BookingCreateSerializer, BookingDatesSerializer, BookingSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from apps.base.stored_procedures import genericDelete
from db_routers.permissions.db_connection import oracle_connection
from rest_framework.decorators import action


class BookingViewSet(viewsets.GenericViewSet):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = BookingSerializers
    filterset_class  = BookingFilter
    search_fields = ['id']
    ordering_fields = ['id']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ["create"]:
            return BookingCreateSerializer
        elif self.action in ["list"]:
            return BookingSerializers
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
        queryset = Reserva.objects.filter(estado = 'ACTIVO')
        booking = get_object_or_404(queryset, pk=pk)
        serializer = BookingSerializers(booking)
        return Response(serializer.data)

    @action(methods=['GET'],detail=False, url_path = 'search-dates')
    def search_dates(self,request):
        # Recibimos el query param de la petición GET
        pk = request.query_params.get('pk','')
        booking = Reserva.objects.filter(id_viv__id__iexact = pk, estado = 'ACTIVO')
        if booking:
            serializer = BookingDatesSerializer(booking, many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(
            {
                'message':'No hay fechas.'
            },
            status = status.HTTP_400_BAD_REQUEST)

    def create(self,request):
        serializer = BookingCreateSerializer(data = request.data, context = request.data) # Aquí enviariamos el resultado de data
        if serializer.is_valid():
            if serializer.save(): 
                return Response(
                    {
                        'message' : '¡Reserva realizada con éxito!'
                    }, status = status.HTTP_201_CREATED)
        return Response(
            {
                'message' : 'Hay errores en la creación.',
                'errors' : serializer.errors
            }
            , status = status.HTTP_400_BAD_REQUEST)