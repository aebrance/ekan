# Generated by Django 3.2.5 on 2023-01-24 00:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('mail', models.EmailField(max_length=100)),
                ('estado_respuesta', models.CharField(choices=[('Respondida', 'Respondida'), ('No respondida', 'No respondida'), ('En proceso', 'En proceso')], default='No respondida', max_length=15)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField()),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
                ('consulta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_contact.consulta')),
            ],
        ),
    ]
