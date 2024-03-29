from apps.locations.api.filters import CountryFilter
from apps.locations.api.general_serializers import CountrySerializers
from apps.locations.models import Countries
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CountryViewSet(viewsets.GenericViewSet):
    serializer_class = CountrySerializers
    filterset_class  = CountryFilter
    search_fields = ['id']
    ordering_fields = ['id']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ["create"]:
            return None
        elif self.action in ["list"]:
            return CountrySerializers
        return self.serializer_class


    def get_queryset(self):
        return Countries.objects.all()

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
        queryset = Countries.objects.all()
        country = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializers(country)
        return Response(serializer.data)