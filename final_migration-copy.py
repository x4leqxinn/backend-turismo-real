from apps.base.utils.raw_data import get_raw, file_list, BASE_UTILS_DIR
from django.db import migrations
from django.db import connections

def database_call(directory_name : str):
    path = str(BASE_UTILS_DIR) + '/utils/db/' + directory_name
    files = file_list(path)
    for index in range(len(files)):
        with connections['turismo_real'].cursor() as c:
            c.execute(""" {} """.format(get_raw(path, files[index])))

def initial_configs(apps,schema_editor):
    database_call('configs')

def make_triggers(apps,schema_editor):
    database_call('triggers')

def make_packages(apps,schema_editor):
    database_call('packages')

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_initial'),
    ]

    operations = [
        migrations.RunPython(initial_configs),
        migrations.RunPython(make_packages),
        migrations.RunPython(make_triggers)
    ]