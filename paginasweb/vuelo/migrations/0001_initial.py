# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('TipoAvion', models.CharField(max_length=50)),
                ('Matricula', models.CharField(max_length=50)),
                ('propietario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('LugarDespegue', models.CharField(max_length=50)),
                ('LugarDestino', models.CharField(max_length=50)),
                ('Pasajeros', models.CharField(max_length=50)),
                ('fecha_vuelo', models.DateTimeField(default=django.utils.timezone.now)),
                ('avion', models.ForeignKey(null=True, to='vuelo.Avion', blank=True)),
            ],
        ),
    ]
