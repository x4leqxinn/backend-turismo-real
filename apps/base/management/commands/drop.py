from django.core.management.base import BaseCommand, CommandError
from apps.base.utils.drop_tables_script import run_drop_tables

class Command(BaseCommand):
    help = 'Comando que ejecuta un script para eliminar las tablas del schema turismo real'

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument('-d', '--database', type=str, help='Nombre del schema de base de datos', )

    def handle(self, *args, **kwargs):
        database = kwargs['database']
        if not database:
            database = 'turismo_real'
        flag, message = run_drop_tables(database)
        messages = {1 : '¡Nombre de schema incorrecto!', 2 : '¡Primero debe hacer las migraciones para cargar el script!'}
        if(flag):
            return self.stdout.write(self.style.SUCCESS('---- TABLAS ELIMINADAS :D ----'))
        return self.stdout.write(self.style.WARNING(messages[message]))