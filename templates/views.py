from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import threading

def sendEmail(email):
    context = {'mail': "こんにちはホセ、私は私のロシアのバンカーから挨拶を送ります。" }
    template = get_template('emails/verify/verify-account.html')
    content = template.render(context)

    message = EmailMultiAlternatives(
        # Asunto
        'Este es un correo de prueba 死神',
        'turismo.real.servicios',
        # Correo que hace los envios
        settings.EMAIL_HOST_USER,
        # Usuarios a los que se les envia el mail
        [email]
        #cc=[] copia a 
    )

    message.attach_alternative(content, 'text/html')
    message.send()

def index(request):
    if request.method == 'POST':
        mail = request.POST.get('txtMail')
        print('Hola')
        hilo1 = threading.Thread(target=sendEmail,kwargs={'email':mail})
        hilo1.start()
        print('XD')

    return render(request,'index.html',{}) 