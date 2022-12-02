from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from apps.base.models.db_models import Persona, Reserva

def send_email(mail_to:str ,subject:str,booking: Reserva,page:str):
    template = {
        1 : 'emails/create_account/create-account.html',
        2 : '',
        3 : '',
        4 : '',
        5 : '',
        6 : '',
    }.get(page)

    if not template:
        return f"The operation '{page}' is not supported!"

    context = {'booking': Reserva }
    template = get_template(template)
    content = template.render(context)

    message = EmailMultiAlternatives(
        # Asunto
        subject,
        settings.EMAIL_HOST_USER,
        # Correo que hace los envios
        settings.EMAIL_HOST_USER,
        # Usuarios a los que se les envia el mail
        [mail_to]
        #cc=[] copia a 
    )

    message.attach_alternative(content, 'text/html')
    message.send()
    return 'Mail sent successfully.'