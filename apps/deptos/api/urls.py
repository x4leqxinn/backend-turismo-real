from django.urls import path

from apps.deptos.api.depto_views import *


urlpatterns = [
    # Métodos listar y buscar
    path('depto/list/',DeptoListAPIView.as_view(),name='depto-list'),
    path('depto/retrieve/<int:pk>',DeptoRetrieveAPIView.as_view(),name='depto-retrieve'),
    path('depto/interior/list/',InteriorGaleryListAPIView.as_view(),name='interior-list'),
    path('depto/exterior/list/',ExteriorGaleryListAPIView.as_view(),name='exterior-list'),
    path('depto/comment/list/',CommentListAPIView.as_view(),name='comment-list'), 
    path('depto/room/list/',RoomListAPIView.as_view(),name='room-list'),
    path('depto/product-state/list/',ProductStateListAPIView.as_view(),name='product-state-list')
]
