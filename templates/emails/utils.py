from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from apps.base.models.db_models import Reserva

def send_email(mail_to:str,booking:Reserva,page:int):
    """Send an email based on the reservation generated
    Args: 
        mail_to (str): recipient's email
        Reserva (Reserva): booking data
        page (int): Dict key
        
    Returns:
        string (str): State of the process
    """
    option = {
        1 : {'template':'emails/create_account/create-account.html','subject':'Bienvenido'},
        2 : {'template':'emails/create_account/create-account.html','subject':'Bienvenido'},
        3 : {'template':'emails/create_account/create-account.html','subject':'Bienvenido'},
        4 : {'template':'emails/create_account/create-account.html','subject':'Bienvenido'},
        5 : {'template':'emails/create_account/create-account.html','subject':'Bienvenido'},
        6 : {'template':'emails/create_account/create-account.html','subject':'Bienvenido'},
    }.get(page)

    if not option:
        return f"The operation '{page}' is not supported!"

    context = {'booking': Reserva }
    template = get_template(option.template)
    content = template.render(context)

    message = EmailMultiAlternatives(option.subject,settings.EMAIL_HOST_USER,settings.EMAIL_HOST_USER,[mail_to])

    message.attach_alternative(content, 'text/html')
    message.send()
    return 'Mail sent successfully.'