# Generated by Django 4.1.3 on 2022-12-04 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state_code', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=2)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('flag', models.IntegerField()),
                ('wikidataid', models.CharField(blank=True, db_column='wikiDataId', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'db_table': 'cities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('iso3', models.CharField(blank=True, max_length=3, null=True)),
                ('numeric_code', models.CharField(blank=True, max_length=3, null=True)),
                ('iso2', models.CharField(blank=True, max_length=2, null=True)),
                ('phonecode', models.CharField(blank=True, max_length=255, null=True)),
                ('capital', models.CharField(blank=True, max_length=255, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('currency_name', models.CharField(blank=True, max_length=255, null=True)),
                ('currency_symbol', models.CharField(blank=True, max_length=255, null=True)),
                ('tld', models.CharField(blank=True, max_length=255, null=True)),
                ('native', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('subregion', models.CharField(blank=True, max_length=255, null=True)),
                ('timezones', models.TextField(blank=True, null=True)),
                ('translations', models.TextField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('emoji', models.CharField(blank=True, max_length=191, null=True)),
                ('emojiu', models.CharField(blank=True, db_column='emojiU', max_length=191, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField()),
                ('flag', models.IntegerField()),
                ('wikidataid', models.CharField(blank=True, db_column='wikiDataId', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=2)),
                ('fips_code', models.CharField(blank=True, max_length=255, null=True)),
                ('iso2', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=191, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField()),
                ('flag', models.IntegerField()),
                ('wikidataid', models.CharField(blank=True, db_column='wikiDataId', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'states',
                'managed': False,
            },
        ),
    ]
