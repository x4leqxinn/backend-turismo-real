from django.core.management.base import BaseCommand, CommandError
from apps.base.models.db_models import *
from apps.base.utils.seed_script import *
class Command(BaseCommand):
    help = 'Comando que ejecuta un script para cargar la base de datos'

    def handle(self, *args, **options):
        print('Haciendo migraciones')
        # TODO: 
        # Realizar for con la logica de carga de los distintos modelos
        run_seed()
        print('--------- OK ---------')