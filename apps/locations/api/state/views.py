from apps.locations.api.filters import CountryStateFilter
from apps.locations.api.general_serializers import CountryStateSerializers
from apps.locations.models import States
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
