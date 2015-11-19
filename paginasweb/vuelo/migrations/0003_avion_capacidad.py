# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuelo', '0002_auto_20151119_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='avion',
            name='Capacidad',
            field=models.CharField(max_length=50, default=50),
            preserve_default=False,
        ),
    ]
