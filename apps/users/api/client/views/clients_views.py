# Para los viewset
from xmlrpc import client
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

    def get_queryset(self, pk = None):

        # Aquí se debe llamar al procedimiento de listado de todo
        
        if pk is None:
            # Llamamos al procedimiento almacenado que nos devuelve la data
            list = listClient(oracle_connection(1))
            client_list = []
            
            for x in list:
            # Creamos una nueva lista con nuestro modelo Cliente
                client_list.append(Client(resultado=str(x[0])))

            return client_list
        return Client(resultado='Mona_xina')


    def get_object(self,pk):
        # Aquí se define la consulta a un objeto
        return Client(resultado='Mona_xina')


    def list(self,request):
        # Acá los resultados de la consulta los serializamos para ser representados en la web
        serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # Acá el resultado se serializa
        try:
            client = self.get_object(pk)
            client_serializer = self.serializer_class(client)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        #serializer = ClientSerializers(instance=client)
        return Response(client_serializer.data)