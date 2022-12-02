from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from apps.base.models.db_models import Reserva as Booking, Persona as Client, Servicio as Service, DetServMov as Mov, DetProyecto, Empleado, Recepcionista
from apps.users.models import User

def send_email(subject:str,mail_to:str,template:str,data:dict):
    """Send email function
    Args: 
        subject (str): Email subject
        mail_to (str): Person who receives the mail
        template (str): File name
        data (dict): Information to show in the email
    """
    context = data
    template = get_template(template)
    content = template.render(context)
    message = EmailMultiAlternatives(subject,settings.EMAIL_HOST_USER,settings.EMAIL_HOST_USER,[mail_to])
    message.attach_alternative(content, 'text/html')
    message.send()


def generate_notice (email_type:str, page:int, client:Client = None, booking:Booking = None):
    """Generic send an email to users 
    Args: 
        email_type (str): Dict key for business area involved
        page (int): Dict key for page template
        client (Persona): Client data
        booking (Reserva): Booking data
    Returns:
        string (str): State of the process
    """
    # Filter with email type
    options = {
        'service':{
                1 :{'template':['emails/create_account/create-account.html','emails/create_account/create-account.html'],'subject':['Estimado Jorge, su servicio esta lista','Se creado un servicio']}, # TRANSPORTE
                2 :{'template':['emails/create_account/create-account.html','jhdjfkd'],'subject':['Estimado Jorge, su reserva esta lista','Se ha generado una reserva']} # TOUR
            }, 
        'booking':{
                1 :{'template':['emails/create_account/create-account.html','emails/create_account/create-account.html'],'subject':['Estimado Jorge, su reserva esta lista','Se ha generado una reserva']}, # RESERVA
                2 :{'template':['emails/create_account/create-account.html','jhdjfkd'],'subject':['Estimado Jorge, su reserva esta lista','Se ha generado una reserva']}, # Cambio estado Checkin
                3 :{'template':['emails/create_account/create-account.html','jhdjfkd'],'subject':['Estimado Jorge, su reserva esta lista','Se ha generado una reserva']}, # Cambio estado Checkout
            }, 
        'client':{
            1:{'template': 'emails/create_account/create-account.html','subject':'Bienvenido'}, # Registro
            2:{'template': 'emails/create_account/create-account.html','subject':'Contraseña cambiada'} # Cambio de password
        }
    }

    if not options:
        return f"The operation '{email_type}' is not supported!"
    
    if email_type == 'client':
        user = User.objects.filter(person = client).first()
        send_email(
            mail_to=user.email,
            subject=options.get(email_type)[page]['subject'],
            template=options.get(email_type)[page]['template'],
            data={'client': client }
            )
    elif email_type == 'booking':
        
        services = Service.objects.filter(id_reserva = booking.id)
        dwelling = booking.id_viv
        client = booking.id_cli
        receptionist = search_receptionist(dwelling.id)
        services = list_services(services)

        context = {
            'dwelling' : dwelling,
            'client' : client,
            'receptionist': receptionist,
            'services': services
        }

        print(options.get(email_type)[page]['subject'][0])
        
        #######################
        ## Send Emails
        #######################

        ## Client
        user = User.objects.filter(person = client.id).first()
        send_email(
            mail_to=user.email,
            subject=options.get(email_type)[page]['subject'][0],
            template=options.get(email_type)[page]['template'][0],
            data=context
            )

        ## Receptionist
        user = User.objects.filter(person = receptionist.id.id).first() 
        send_email(
            mail_to=user.email,
            subject=options.get(email_type)[page]['subject'][1],
            template=options.get(email_type)[page]['template'][1],
            data=context
        )
        
        if page == 1 and services:
            ## Drivers
            for x in range(len(services)):
                user = User.objects.filter(person = services[x].get('driver').id.id).first()
                send_email(
                    mail_to=user.email,
                    subject=options.get('service')[1]['subject'][1],
                    template=options.get('service')[1]['template'][1],
                    data=context
                )
    return 'Mail sent successfully.'


def search_receptionist(dwelling_id):
    queryset =  DetProyecto.objects.filter(id_viv = dwelling_id)
    response = None

    for index in range(len(queryset)):
        if queryset[index].id_emp.id_car.id == 3:
            # Obtenemos la instancia de empleado y luego de recepcionista
            employee = Empleado.objects.get(id = queryset[index].id_emp.id)
            receptionist = Recepcionista.objects.get(id = employee)
            response = receptionist
            break
    return response


def list_services(services):
    service_list = []
    for x in range(len(services)):
        detail_service = Mov.objects.filter(id_mov = services[x].id).first()
        data = {
            'id_service' : detail_service.id_mov,
            'driver' : detail_service.id_con,
            'start_date' : detail_service.fecha_inicio,
            'start_time' : detail_service.hora_inicio,
            'end_date' : detail_service.fecha_termino,
            'end_time' : detail_service.hora_termino,
            'passengers' : detail_service.cant_pasajeros
        }
        service_list.append(data)
    return service_list





def booking_email(mail_to:str,booking:Booking,page:int):
    def decorator_function(original_function):

        # Función decorada
        def wrapper_function(*args, **kwargs):
            result = original_function(*args, **kwargs)

            # Enviamos un correo al finalizar la operacion
            send_email(mail_to,booking,page)
            return result

        return wrapper_function
    return decorator_function

# Un decorador nos permite ejecutar código antes o después de la función
#@prefix_decorator(nombre='Jorge')