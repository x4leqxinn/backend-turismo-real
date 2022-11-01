from django.core.management.base import BaseCommand, CommandError
from apps.base.models.db_models import *
from apps.base.utils.seed_script import *
class Command(BaseCommand):
    help = 'Comando que ejecuta un script para cargar la base de datos'

    def handle(self, *args, **options):
        print('--------- Realizando migraciones ---------')
        run_seed()
        print('--------- OK ---------')