# Auth Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from apps.users.auth.auth_filters import UserFilter
from apps.users.auth.auth_serializers import PasswordSerializer, UserListSerializer
from apps.users.auth.authentication_mixins import Authentication
from django.shortcuts import get_object_or_404

# Manejo de sesiones
from datetime import datetime
from django.contrib.sessions.models import Session


# HTTP Responses
from rest_framework.response import Response
from rest_framework import status

# APIView
from rest_framework.views import APIView

from rest_framework import viewsets

from apps.users.models import User

from rest_framework.decorators import action

# from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


'''
Método que elimina todas las sesiones activas asociadas a un usuario
{params} : user : str
{params} : token : str
'''
def closeSessions(user,token):
    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
    if all_sessions.exists():
        for session in all_sessions:
            session_data = session.get_decoded()
            if str(user.id) == str(session_data.get('_auth_user_id')):
                session.delete()
    token.delete()


class UserToken(Authentication,APIView):

    def get(self,request,*args,**kwargs):
        try:
            # Recibimos o creamos el token del usuario asociado
            user_token,_ = Token.objects.get_or_create(user = self.user)
            user = UserListSerializer(self.user)
            return Response({
                'token' : user_token.key,
                'user' : user.data
            })
        except:
            # Si no se encuentra usuario
            return Response({
                'error' : 'Credenciales enviadas incorrectas.',
            }, status = status.HTTP_400_BAD_REQUEST
            )


class Login(ObtainAuthToken):
    '''
        Login request 
        {params} username : str {email}
        {params} password : str {password}
    '''

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request' : request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            user_serializer = UserListSerializer(user)

            # Sólo se puede iniciar sesión si el usuario está activo
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                if created:
                    return Response({
                        'token' : token.key,
                        'user' : user_serializer.data,
                        'message' : 'Inicio de sesión éxitoso.'
                    }, status=status.HTTP_201_CREATED)
                else:
                    # Se cierran todas las sesiones activas
                    closeSessions(user,token)
                    # Se crea un nuevo token de sesión
                    token = Token.objects.create(user=user)
                    return Response({
                        'token' : token.key,
                        'user' : user_serializer.data,
                        'message' : 'Inicio de sesión éxitoso'
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error' : 'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error' : 'Correo electrónico o contraseña incorrectos'}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error' : 'Información enviada no válida'}, status = status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    '''
        Logout request 
        {params} token : str {token}
    '''
    def post(self, request, *args, **kwargs):
        try:
            token = request.data['token']
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user
                closeSessions(user,token)
                session_message = 'Sesiones de usuario eliminadas'
                token_message = 'Token eliminado'
                return Response({'token_message' : token_message, 'session_message' : session_message},status = status.HTTP_200_OK)
            return Response({'error' : 'No se ha encontrado un usuario con estas credenciales.'}, status = status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({'error' : 'No se ha encontrado token en la petición.'}, status = status.HTTP_409_CONFLICT)
class AccountUserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserListSerializer
    filterset_class  = UserFilter
    search_fields = ['email','id']
    ordering_fields = ['email','id']
    ordering = ['id']


    def get_serializer_class(self):
        if self.action in ["create"]:
            return None
        elif self.action in ["list"]:
            return UserListSerializer
        return self.serializer_class

    def get_object(self,pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        return User.objects.filter(is_active = True)

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


    # Detail obligatorio, le agrega un campo id
    @action(detail=True, methods=['POST'], url_path='change-password')
    def set_password(self,request,pk = None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data = request.data)
        if password_serializer.is_valid():
            print(password_serializer.validated_data['password'])
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': 'Contraseña actualizada correctamente.'
            }, status = status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la información enviada.',
            'errors' : password_serializer.errors
        }, status = status.HTTP_400_BAD_REQUEST)
