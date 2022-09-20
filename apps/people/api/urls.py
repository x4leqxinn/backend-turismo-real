from django.urls import path

from apps.people.api.gender.views import *
from apps.people.api.identification_document.views import *
from apps.people.api.marital_status.views import *


urlpatterns = [
    # Métodos listar
    path('gender/list/',GenderAPIView.as_view(),name='gender-list'),
    path('identification-document/list/',IdentificationDocumentAPIView.as_view(),name='identification-list'),
    path('marital-status/list/',MaritalStatusAPIView.as_view(),name='marital-list'),

]
