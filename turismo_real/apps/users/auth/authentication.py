from datetime import timedelta
from django.utils import timezone

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header

from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self,token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self,token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            # Si ha expirado lo eliminamos y creamos un nuevo token
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)
        return token
    
    # Verificamos si el usuario está autenticado
    def authenticate_credentials(self, key):
        token, user = None, None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
            # Verificamos si el token ha expirado
            token = self.token_expire_handler(token)
        except self.get_model().DoesNotExist:
            pass
        return user