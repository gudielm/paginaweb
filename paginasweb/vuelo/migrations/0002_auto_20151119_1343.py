# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuelo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('NombreAero', models.CharField(max_length=50)),
                ('Ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='avion',
            old_name='nombre',
            new_name='Nombre',
        ),
        migrations.RenameField(
            model_name='avion',
            old_name='propietario',
            new_name='Propietario',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='avion',
        ),
        migrations.AddField(
            model_name='vuelo',
            name='Avion',
            field=models.ForeignKey(to='vuelo.Avion', default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vuelo',
            name='NumeroVuelo',
            field=models.CharField(max_length=10, default=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='LugarDespegue',
            field=models.ForeignKey(to='vuelo.Aeropuerto'),
        ),
    ]
