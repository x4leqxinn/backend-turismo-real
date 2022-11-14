# Generated by Django 4.1.3 on 2022-11-13 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='travels/')),
                ('id_ciu', models.IntegerField()),
                ('id_est', models.IntegerField()),
                ('id_pai', models.IntegerField()),
            ],
            options={
                'db_table': 'destino',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'db_table': 'documento',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstadoProducto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('abono', models.IntegerField()),
                ('monto_pagado', models.IntegerField()),
                ('total_pago', models.BigIntegerField()),
                ('cant_acompaniante', models.IntegerField()),
                ('cant_total', models.IntegerField()),
                ('id_cli', models.ForeignKey(db_column='id_cli', on_delete=django.db.models.deletion.DO_NOTHING, to='people.cliente')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'db_table': 'reserva',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'db_table': 'sala',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('precio', models.IntegerField()),
                ('id_reserva', models.ForeignKey(db_column='id_reserva', on_delete=django.db.models.deletion.DO_NOTHING, to='business.reserva')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'servicio',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('calle', models.CharField(max_length=20)),
                ('num_calle', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('id_pai', models.IntegerField()),
                ('id_est', models.IntegerField()),
                ('id_ciu', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de documento',
                'verbose_name_plural': 'Tipos de documentos',
                'db_table': 'tipo_documento',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoMulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Multa',
                'verbose_name_plural': 'Tipos de Multa',
                'db_table': 'tipo_multa',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de servicio',
                'verbose_name_plural': 'Tipos de servicios',
                'db_table': 'tipo_servicio',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoUbicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tipo de ubicación',
                'verbose_name_plural': 'Tipos de ubicaciones',
                'db_table': 'tipo_ubicacion',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo Vivienda',
                'verbose_name_plural': 'Tipos de Vivienda',
                'db_table': 'tipo_vivienda',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TramoAbono',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('monto_inf', models.IntegerField()),
                ('monto_sup', models.IntegerField()),
                ('porcentaje', models.IntegerField()),
                ('estado', models.CharField(max_length=15)),
                ('creacion', models.DateTimeField()),
                ('actualizacion', models.DateTimeField()),
            ],
            options={
                'db_table': 'tramo_abono',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TramoMulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('estado_prod', models.IntegerField()),
                ('porcentaje', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Tramo de multa',
                'verbose_name_plural': 'Tramos de multas',
                'db_table': 'tramo_multa',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DCheck',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.documento')),
            ],
            options={
                'verbose_name': 'Documento de Check',
                'verbose_name_plural': 'Documentos de Check',
                'db_table': 'd_check',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movilizacion',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.servicio')),
            ],
            options={
                'verbose_name': 'Servicio de Movilización',
                'verbose_name_plural': 'Servicios de Movilización',
                'db_table': 'movilizacion',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('latitud', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=100)),
                ('m2', models.CharField(max_length=30)),
                ('estrellas', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=30)),
                ('imagen_principal', models.ImageField(upload_to='viviendas/')),
                ('valor_noche', models.IntegerField()),
                ('abono_base', models.IntegerField()),
                ('id_pai', models.IntegerField()),
                ('id_est', models.IntegerField()),
                ('id_ciu', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('internet', models.CharField(max_length=1)),
                ('agua', models.CharField(max_length=1)),
                ('luz', models.CharField(max_length=1)),
                ('gas', models.CharField(max_length=1)),
                ('id_dis', models.ForeignKey(db_column='id_dis', on_delete=django.db.models.deletion.DO_NOTHING, to='base.disponibilidad')),
                ('id_tip', models.ForeignKey(db_column='id_tip', on_delete=django.db.models.deletion.DO_NOTHING, to='business.tipovivienda')),
            ],
            options={
                'verbose_name': 'Vivienda',
                'verbose_name_plural': 'Viviendas',
                'db_table': 'vivienda',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UbicacionTrans',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('id_ciu', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('latitud', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=100)),
                ('id_tip', models.ForeignKey(db_column='id_tip', on_delete=django.db.models.deletion.DO_NOTHING, to='business.tipoubicacion')),
            ],
            options={
                'verbose_name': 'Ubicación de transporte',
                'verbose_name_plural': 'Ubicaciones de transporte',
                'db_table': 'ubicacion_trans',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='servicio',
            name='id_tip',
            field=models.ForeignKey(db_column='id_tip', on_delete=django.db.models.deletion.DO_NOTHING, to='business.tiposervicio'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='id_viv',
            field=models.ForeignKey(db_column='id_viv', on_delete=django.db.models.deletion.DO_NOTHING, to='business.vivienda'),
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('estrellas', models.CharField(max_length=1)),
                ('id_cli', models.ForeignKey(db_column='id_cli', on_delete=django.db.models.deletion.DO_NOTHING, to='people.cliente')),
                ('id_viv', models.ForeignKey(db_column='id_viv', on_delete=django.db.models.deletion.DO_NOTHING, to='business.vivienda')),
            ],
            options={
                'verbose_name': 'Puntuación',
                'verbose_name_plural': 'Puntuaciones',
                'db_table': 'puntuacion',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('id_cat', models.ForeignKey(db_column='id_cat', on_delete=django.db.models.deletion.DO_NOTHING, to='base.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('id_viv', models.OneToOneField(db_column='id_viv', on_delete=django.db.models.deletion.DO_NOTHING, to='business.vivienda')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
                'db_table': 'inventario',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='documento',
            name='id_tip',
            field=models.ForeignKey(db_column='id_tip', on_delete=django.db.models.deletion.DO_NOTHING, to='business.tipodocumento'),
        ),
        migrations.CreateModel(
            name='DetProyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('id_emp', models.ForeignKey(db_column='id_emp', on_delete=django.db.models.deletion.DO_NOTHING, to='people.empleado')),
                ('id_viv', models.ForeignKey(db_column='id_viv', on_delete=django.db.models.deletion.DO_NOTHING, to='business.vivienda')),
            ],
            options={
                'verbose_name': 'Detalle del proyecto',
                'verbose_name_plural': 'Detalles del proyecto',
                'db_table': 'det_proyecto',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetalleSala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('imagen_sala', models.ImageField(upload_to='rooms/')),
                ('id_inv', models.ForeignKey(db_column='id_inv', on_delete=django.db.models.deletion.DO_NOTHING, to='business.inventario')),
                ('id_sal', models.ForeignKey(db_column='id_sal', on_delete=django.db.models.deletion.DO_NOTHING, to='business.sala')),
            ],
            options={
                'verbose_name': 'Detalle de sala',
                'verbose_name_plural': 'Detalles de salas',
                'db_table': 'detalle_sala',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetalleProducto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('id_det', models.ForeignKey(db_column='id_det', on_delete=django.db.models.deletion.DO_NOTHING, to='business.detallesala')),
                ('id_est', models.ForeignKey(db_column='id_est', on_delete=django.db.models.deletion.DO_NOTHING, to='business.estadoproducto')),
                ('id_pro', models.ForeignKey(db_column='id_pro', on_delete=django.db.models.deletion.DO_NOTHING, to='business.producto')),
            ],
            options={
                'verbose_name': 'Detalle de producto',
                'verbose_name_plural': 'Detalles de productos',
                'db_table': 'detalle_producto',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('monto_final', models.IntegerField()),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='people.cliente')),
                ('id_reserva', models.OneToOneField(db_column='id_reserva', on_delete=django.db.models.deletion.DO_NOTHING, to='business.reserva')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'compra',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('fecha_salida', models.DateField()),
                ('hora_salida', models.CharField(max_length=5)),
                ('estado_checkout', models.CharField(max_length=30)),
                ('total_multa', models.IntegerField(blank=True, null=True)),
                ('id_rec', models.ForeignKey(db_column='id_rec', on_delete=django.db.models.deletion.DO_NOTHING, to='people.recepcionista')),
                ('id_res', models.OneToOneField(db_column='id_res', on_delete=django.db.models.deletion.DO_NOTHING, to='business.reserva')),
            ],
            options={
                'verbose_name': 'Check Out',
                'verbose_name_plural': 'Check Out',
                'db_table': 'check_out',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('fecha_llegada', models.DateField()),
                ('hora_llegada', models.CharField(max_length=5)),
                ('firma', models.CharField(max_length=1, null=True)),
                ('estado_checkin', models.CharField(max_length=30)),
                ('id_rec', models.ForeignKey(db_column='id_rec', on_delete=django.db.models.deletion.DO_NOTHING, to='people.recepcionista')),
                ('id_res', models.OneToOneField(db_column='id_res', on_delete=django.db.models.deletion.DO_NOTHING, to='business.reserva')),
            ],
            options={
                'verbose_name': 'Check In',
                'verbose_name_plural': 'Check In',
                'db_table': 'check_in',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.movilizacion')),
            ],
            options={
                'verbose_name': 'Servicio de Tour',
                'verbose_name_plural': 'Servicios de Tours',
                'db_table': 'tour',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.movilizacion')),
            ],
            options={
                'verbose_name': 'Servicio de transporte',
                'verbose_name_plural': 'Servicios de transporte',
                'db_table': 'transporte',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetServMov',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('fecha_inicio', models.DateField()),
                ('hora_inicio', models.CharField(max_length=5)),
                ('fecha_termino', models.DateField()),
                ('hora_termino', models.CharField(max_length=5)),
                ('cant_pasajeros', models.IntegerField()),
                ('id_con', models.ForeignKey(db_column='id_con', on_delete=django.db.models.deletion.DO_NOTHING, to='people.conductor')),
                ('id_mov', models.ForeignKey(db_column='id_mov', on_delete=django.db.models.deletion.DO_NOTHING, to='business.movilizacion')),
            ],
            options={
                'verbose_name': 'Detalles de servicio de Movilización',
                'verbose_name_plural': 'Detalle de servicios de Movilización',
                'db_table': 'det_serv_mov',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DCoordinacion',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.documento')),
                ('id_mov', models.OneToOneField(db_column='id_mov', on_delete=django.db.models.deletion.DO_NOTHING, to='business.movilizacion')),
            ],
            options={
                'verbose_name': 'Documento de Coodinación',
                'verbose_name_plural': 'Documentos de Coodinación',
                'db_table': 'd_coordinacion',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TransporteVuelta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('id_ub_trans', models.ForeignKey(db_column='id_ub_trans', on_delete=django.db.models.deletion.DO_NOTHING, to='business.ubicaciontrans')),
                ('id_trans', models.OneToOneField(db_column='id_trans', on_delete=django.db.models.deletion.DO_NOTHING, to='business.transporte')),
            ],
            options={
                'verbose_name': 'Servicio de transporte de vuelta',
                'verbose_name_plural': 'Servicios de transportes de vuelta',
                'db_table': 'transporte_vuelta',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TransporteIda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('id_ub_trans', models.ForeignKey(db_column='id_ub_trans', on_delete=django.db.models.deletion.DO_NOTHING, to='business.ubicaciontrans')),
                ('id_trans', models.OneToOneField(db_column='id_trans', on_delete=django.db.models.deletion.DO_NOTHING, to='business.transporte')),
            ],
            options={
                'verbose_name': 'Servicio de transporte de ida',
                'verbose_name_plural': 'Servicios de transportes de ida',
                'db_table': 'transporte_ida',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.dcheck')),
                ('id_che', models.OneToOneField(db_column='id_che', on_delete=django.db.models.deletion.DO_NOTHING, to='business.checkout')),
            ],
            options={
                'verbose_name': 'Documento de Check-out',
                'verbose_name_plural': 'Documentos de Check-out',
                'db_table': 'salida',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.dcheck')),
                ('id_che', models.OneToOneField(db_column='id_che', on_delete=django.db.models.deletion.DO_NOTHING, to='business.checkin')),
            ],
            options={
                'verbose_name': 'Documento de Check-in',
                'verbose_name_plural': 'Documentos de Check-in',
                'db_table': 'registro',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetalleTour',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(default='ACTIVO', max_length=15)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('id_des', models.ForeignKey(db_column='id_des', on_delete=django.db.models.deletion.DO_NOTHING, to='business.destino')),
                ('id_tou', models.ForeignKey(db_column='id_tou', on_delete=django.db.models.deletion.DO_NOTHING, to='business.tour')),
            ],
            options={
                'verbose_name': 'Detalle de Tour',
                'verbose_name_plural': 'Detalles de Tours',
                'db_table': 'detalle_tour',
                'ordering': ['id'],
                'managed': True,
            },
        ),
    ]
