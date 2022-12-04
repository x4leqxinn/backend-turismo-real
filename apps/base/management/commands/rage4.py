from django.core.management.base import BaseCommand, CommandError
from apps.base.models.db_models import *
import os
class Command(BaseCommand):
    help = 'Comando que ejecuta un script para eliminar las migraciones'

    def handle(self, *args, **options):
        os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
        os.system('find . -path "*/migrations/*.pyc"  -delete')
        os.system('pip install --upgrade --force-reinstall  Django==4.1.3')
        self.stdout.write(self.style.SUCCESS('--------- Ya te desesperaste demasiado :P ---------'))
