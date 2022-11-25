from django.core.management.base import BaseCommand
from apps.base.utils.create_schema_script import run_create_schema
from apps.base.utils.drop_schema_script import run_drop_schema

class Command(BaseCommand):
    help = 'Comando que crea la base de datos de turismo real'


    def handle(self, *args, **kwargs):
        ## Debe intentar borrar el schema
        run_drop_schema()
        ## Se debe crear el schema
        run_create_schema()
        return self.stdout.write(self.style.SUCCESS('--- BASE DE DATOS REINICIADA ---'))