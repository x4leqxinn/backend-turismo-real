from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .emails.utils import prefix_decorator
from apps.base.models.db_models import Reserva, CheckIn, CheckOut, Servicio, Compra
from django.views.generic import CreateView, ListView, DeleteView, View
from apps.users.models import User
from datetime import datetime


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

#reserva = Reserva.objects.filter(id=1).first()

#@prefix_decorator(email_type='booking',page=1,booking=reserva)
def index(request):
    print('Hola')
    if request.method == 'POST':
        mail = request.POST.get('txtMail')
        

    return render(request,'index.html',{}) 


import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
class BookingPdf(View):

    def link_callback(self,uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
                if not isinstance(result, (list, tuple)):
                        result = [result]
                result = list(os.path.realpath(path) for path in result)
                path=result[0]
        else:
                sUrl = settings.STATIC_URL        # Typically /static/
                sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                mUrl = settings.MEDIA_URL         # Typically /media/
                mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                if uri.startswith(mUrl):
                        path = os.path.join(mRoot, uri.replace(mUrl, ""))
                elif uri.startswith(sUrl):
                        path = os.path.join(sRoot, uri.replace(sUrl, ""))
                else:
                        return uri

        # make sure that file exists
        if not os.path.isfile(path):
                raise Exception(
                        'media URI invalid'
                )
        return path

    def get(self,request,*args,**kwargs):
        #Importamos primeramente date, para poder manejar el formato "fechas"
        #from datetime import date
        # Find the template and render it
        template = get_template('reports/booking.html')
        booking = Reserva.objects.filter(id=self.kwargs['pk']).first()
        client = booking.id_cli.id
        checkin = CheckIn.objects.get(id_res=booking)
        checkout = CheckOut.objects.get(id_res=booking)
        services = Servicio.objects.filter(id_reserva=booking.id)
        user = User.objects.get(person=client)
        dwelling = booking.id_viv
        nights = (booking.fecha_termino - booking.fecha_inicio).days + 1
        purchase = Compra.objects.get(id_reserva=booking)
        paid_out = True if booking.total_pago == booking.monto_pagado else False
        now = datetime.now()
        context = {
            'booking': booking,
            'checkin': checkin,
            'checkout': checkout,
            'client': client,
            'dwelling': dwelling,
            'services': services,
            'user': user,
            'nights': nights,
            'purchase': purchase,
            'paid_out': paid_out,
            'created_at': now,
            'STATIC_ROOT': settings.STATIC_ROOT
        }
        html = template.render(context)
        # Create a django response object
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Create a PDF
        pisa_status = pisa.CreatePDF(
            html, dest=response,
            #link_callback=self.link_callback
        )
        if pisa_status.err:
            return HttpResponse('We had sime errors <pre>'+ html + '</pre>')
        return response
