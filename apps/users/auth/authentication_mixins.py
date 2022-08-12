from rest_framework.authentication import get_authorization_header
from apps.users.auth.authentication import ExpiringTokenAuthentication
from rest_framework import status, exceptions
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


# authentication.BaseAuthentication
class Authentication(object):
    user = None
    
    def get_user(self, request):
        # Recibimos el token de los headers
        token = get_authorization_header(request).split()
        
        # Si existe el valor lo parseamos
        if token:
            try:
                token = token[1].decode()
            except:
                return None

            # Verificamos la expiración y obtenemos el usuario asociado
            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)

            if user != None:
                self.user = user
                return user
                
        return None

    def dispatch(self,request,*args,**kwargs):
        user = self.get_user(request)
        # Encontró el token en el request
        if user is not None:
            return super().dispatch(request,*args,**kwargs)

        # No encontró token en el request
        response = Response({'error' : 'No se han enviado las credenciales.'}, 
                            status = status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response