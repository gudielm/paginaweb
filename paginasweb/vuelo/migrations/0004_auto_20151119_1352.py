# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuelo', '0003_avion_capacidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelo',
            name='LugarDestino',
            field=models.ForeignKey(related_name='Aeropuerto2', to='vuelo.Aeropuerto'),
        ),
    ]
