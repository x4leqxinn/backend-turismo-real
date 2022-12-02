from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from apps.base.models.db_models import Persona

def send_email(email : str ,asunto : str,cliente : Persona, page : str):
    context = {'cliente': cliente }
    template = get_template('emails/create_account/create-account.html') #emails/verify/verify-account.html
    content = template.render(context)

    message = EmailMultiAlternatives(
        # Asunto
        asunto,
        settings.EMAIL_HOST_USER,
        # Correo que hace los envios
        settings.EMAIL_HOST_USER,
        # Usuarios a los que se les envia el mail
        [email]
        #cc=[] copia a 
    )

    message.attach_alternative(content, 'text/html')
    message.send()
