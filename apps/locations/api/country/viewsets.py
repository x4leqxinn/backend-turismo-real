# Para los viewset
from rest_framework import viewsets
from rest_framework.response import Response
# Para usar status codes
from rest_framework import status

from apps.locations.general_serializers import CountrySerializers
from apps.locations.models import Pais

from db_routers.permissions.db_connection import *
from apps.locations.api.country.connections.country_sp import *

class CountryViewSet(viewsets.GenericViewSet):

    serializer_class = CountrySerializers

    def get_queryset(self, pk = None):
        # Aquí se debe llamar al procedimiento de listado de todo 
        if pk is None:
            # Llamamos al procedimiento almacenado que nos devuelve la data
            list = listCountry(oracle_connection(1))
            country_list = []
            
            for x in list:
                c = Pais()
                c.id = x[0]
                c.cod_pais = x[1]
                c.nombre = x[2]
                c.cod_tel = x[3]
                c.bandera = x[4]
                # Creamos una nueva lista con nuestro modelo
                country_list.append(c)

            return country_list
        return Pais(id=1)

    
    def get_object(self,pk):
        # Aquí se define la consulta a un objeto
        data = retrieveCountry(oracle_connection(1),pk)  
        c = Pais()
        c.id = data[0][0]
        c.cod_pais = data[0][1]
        c.nombre = data[0][2]
        c.cod_tel = data[0][3]      
        c.bandera = data[0][4]
        return c


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