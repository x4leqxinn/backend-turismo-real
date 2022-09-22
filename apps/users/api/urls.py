from django.urls import path

from apps.users.api.client.views.clients_views import *


urlpatterns = [
    # Métodos listar y buscar
    path('client/list/',ClientListAPIView.as_view(),name='country-list'),
    #path('country/retrieve/<int:pk>',CountryRetrieveAPIView.as_view(),name='country-retrieve'),
]
