# Para los viewset
from rest_framework.response import Response
# Para usar status codes
from rest_framework import status

from rest_framework import generics
from apps.employees.employee_serializers import EmployeeSerializers
from apps.base.models.db_models import Empleado
from apps.employees.api.filters import EmployeeFilter


from rest_framework import viewsets
from rest_framework.decorators import action

 
# LISTAR CLIENTES
class EmployeeViewSet(viewsets.GenericViewSet):
    serializer_class = EmployeeSerializers
    filterset_class  = EmployeeFilter
    search_fields = ['nombre','id']
    ordering_fields = ['nombre','id']
    ordering = ['id']

    def get_queryset(self):
        return  Empleado.objects.filter(id__estado = 'ACTIVO')

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
