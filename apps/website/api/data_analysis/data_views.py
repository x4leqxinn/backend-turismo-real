from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.website.api.data_analysis.data_serializers import *
from apps.website.api.data_analysis.data_filter import *

class DataframeViewset(viewsets.GenericViewSet):
    #authentication_classes = ()
    #permission_classes = ()
    serializer_class = DataframeSerializer
    filterset_class  = DataframeFilter
    search_fields = ['id']
    ordering_fields = ['id']
    ordering = ['id']

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()

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
        dataframe = get_object_or_404(self.queryset, pk=pk)
        serializer = DataframeSerializer(dataframe)
        return Response(serializer.data)
