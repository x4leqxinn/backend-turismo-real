from apps.base.models.db_models import Reserva
from apps.business.api.general_filters import BookingFilter
from apps.business.api.shopping.shopping_serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from apps.base.stored_procedures import genericDelete
from db_routers.permissions.db_connection import oracle_connection
from rest_framework.decorators import action


class ShoppingViewSet(viewsets.GenericViewSet):
    serializer_class = CreateShoppingSerializer
    filterset_class  = BookingFilter
    search_fields = ['id']
    ordering_fields = ['id']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ["booking_payment"]:
            return CreateShoppingSerializer
        elif self.action in ["list"]:
            return CreateShoppingSerializer
        elif self.action in ["service_payment"]:
            return ServicePaymentSerializer
        return self.serializer_class

    @action(methods=['post'],detail=False, url_path = 'booking-payment')
    def booking_payment(self,request):
        serializer = CreateShoppingSerializer(data = request.data, context = request.data) # Aquí enviariamos el resultado de data
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
    
    @action(methods=['POST'],detail=False, url_path = 'service-payment')
    def service_payment(self,request):
        serializer = ServicePaymentSerializer(data = request.data, context = request.data) # Aquí enviariamos el resultado de data
        if serializer.is_valid():
            if serializer.save(): 
                return Response(
                    {
                        'message' : '¡Servicios comprados!'
                    }, status = status.HTTP_201_CREATED)
        return Response(
            {
                'message' : 'Hay errores en la creación.',
                'errors' : serializer.errors
            }
            , status = status.HTTP_400_BAD_REQUEST)


    @action(methods=['POST'],detail=False, url_path = 'add-companion')
    def add_companion(self,request):
        serializer = AddCompanionSerializer(data = request.data, context = request.data) 
        if serializer.is_valid():
            if serializer.save(): 
                return Response(
                    {
                        'message' : '¡Acompañantes agregados correctamente!'
                    }, status = status.HTTP_201_CREATED)
        return Response(
            {
                'message':'Hay errores en la creación.',
                'errors' : serializer.errors
            },status=status.HTTP_400_BAD_REQUEST
        )

    @action(methods=['POST'],detail=False, url_path = 'suscription-payment')
    def suscription_payment(self,request):
        serializer = SuscriptionPaymentSerializer(data = request.data, context = request.data) 
        if serializer.is_valid():
            if serializer.save(): 
                return Response(
                    {
                        'message' : '¡Pago realizado con éxito!'
                    }, status = status.HTTP_201_CREATED)
        return Response(
            {
                'message':'Hay errores en la creación.',
                'errors' : serializer.errors
            },status=status.HTTP_400_BAD_REQUEST
        )