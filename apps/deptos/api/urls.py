from django.urls import path

from apps.deptos.api.depto_views import *


urlpatterns = [
    # Métodos listar y buscar
    path('depto/list/',DeptoListAPIView.as_view(),name='depto-list'),
    path('depto/retrieve/<int:pk>',DeptoRetrieveAPIView.as_view(),name='depto-retrieve'),
]
