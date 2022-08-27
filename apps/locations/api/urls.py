from django.urls import path

from apps.locations.api.country.views import *

urlpatterns = [
    # Métodos listar y buscar
    path('country/list/',CountryListAPIView.as_view(),name='country-list'),
    path('country/retrieve/<int:pk>',CountryRetrieveAPIView.as_view(),name='country-retrieve'),
]
