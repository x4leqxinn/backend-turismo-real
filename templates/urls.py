from django.urls import path
from templates.views import index

urlpatterns = [
    path('email/',index, name = 'email'),
]
