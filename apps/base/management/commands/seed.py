from django.core.management.base import BaseCommand, CommandError
from apps.base.models.db_models import *
from apps.base.utils.seed_script import *
class Command(BaseCommand):
    help = 'Comando que ejecuta un script para cargar la base de datos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('--------- Realizando migraciones ---------'))
        run_seed()
        self.stdout.write(self.style.SUCCESS('--------- OK ---------'))