# Para los viewset
from rest_framework import viewsets

from rest_framework.response import Response
# Para usar status codes
from rest_framework import status

from apps.users.api.client.serializers.clients_serializers import *

from apps.users.api.client.models.models import *

from apps.users.db_routers.db_connection import *
from apps.users.api.client.connections.clients_sp import *

class ClientViewSet(viewsets.GenericViewSet):
    serializer_class = ClientSerializers

    queryset = []

    '''
    def get_queryset(self, pk = None):
        if pk is None:
            datita = {'resultado' : 'comiste comia'}
            return self.get_serializer(data = datita)
        print('FFFFF')
        datita = [{'resultado' : 'XDDD'}]
        return self.get_serializer(datta = datita)
    '''


    def list(self,request):

        listClient(oracle_connection(1));

        clients = {
            'ew' : Client(resultado  = 'Joaquín Reyes'),
            2 : Client(resultado  = 'Paula Piña'),
            3 : Client(resultado  = 'Lucas Menares'),
            4 : Client(resultado  = 'Paula Soto'),
            1 : Client(resultado  = 'Jorge Quintui'),
        }

        client_serializer = ClientSerializers(
            instance = clients.values(),many=True
        )
        return Response(client_serializer.data, status = status.HTTP_200_OK)