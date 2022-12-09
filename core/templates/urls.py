from django.urls import path
from core.templates.views import index
from core.templates.views import BookingPdf
urlpatterns = [
    path('email/',index, name = 'email'),
    path('reporte/<int:pk>/',BookingPdf.as_view(), name = 'reporte'),
]
