# Generated by Django 4.2.2 on 2023-06-20 18:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('habitacionId', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.PositiveSmallIntegerField(unique=True)),
                ('piso', models.PositiveSmallIntegerField()),
                ('estado', models.CharField(default='Disponible', max_length=50)),
                ('precio', models.IntegerField()),
                ('tipoHabitacion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Habitaciones de un hotel',
                'verbose_name_plural': 'Habitaciones',
                'db_table': 'Habitacion',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='img/habitaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('servicioId', models.AutoField(primary_key=True, serialize=False)),
                ('servicio', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Servicios que contienen las habitaciones de un hotel',
                'verbose_name_plural': 'Servicios',
                'db_table': 'Servicio',
            },
        ),
        migrations.CreateModel(
            name='ServicioPorHabitacion',
            fields=[
                ('servicioPorHabitacionId', models.AutoField(primary_key=True, serialize=False)),
                ('habitacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionReservas.habitacion')),
                ('servicioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionReservas.servicio')),
            ],
            options={
                'verbose_name': 'Servicio de cada habitación',
                'verbose_name_plural': 'ServiciosPorHabitacion',
                'db_table': 'ServicioPorHabitacion',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('reservaId', models.AutoField(primary_key=True, serialize=False)),
                ('fechaReserva', models.DateField(default=datetime.date.today)),
                ('fechaIngreso', models.DateField()),
                ('fechaEgreso', models.DateField()),
                ('habitacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionReservas.habitacion')),
            ],
            options={
                'verbose_name': 'Reservas de habitacinoes en un hotel',
                'verbose_name_plural': 'Reservas',
                'db_table': 'Reserva',
            },
        ),
    ]
