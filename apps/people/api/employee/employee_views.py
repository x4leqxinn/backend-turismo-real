# Para los viewset
from rest_framework.response import Response
from apps.people.api.employee.employee_serializers import EmployeeSerializers
from apps.base.models.db_models import Empleado
from apps.people.api.filters import EmployeeFilter
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


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

    def retrieve(self, request, pk=None):
        queryset = Empleado.objects.filter(id__estado = 'ACTIVO')
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)