from django.urls import path

from apps.locations.api.country.views import *
from apps.locations.api.state.views import *
from apps.locations.api.city.views import *

urlpatterns = [
    # Métodos listar y buscar
    path('country/list/',CountryListAPIView.as_view(),name='country-list'),
    path('country/retrieve/<int:pk>',CountryRetrieveAPIView.as_view(),name='country-retrieve'),
    path('country-state/list/',CountryStateListAPIView.as_view(),name='country-state-list'),
    path('country-state/retrieve/<int:pk>',CountryStateRetrieveAPIView.as_view(),name='country-state-retrieve'),
    path('city/list/',CityListAPIView.as_view(),name='city-list'),
    path('city/retrieve/<int:pk>',CityRetrieveAPIView.as_view(),name='city-retrieve'),
]
