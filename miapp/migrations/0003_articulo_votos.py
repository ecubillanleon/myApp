# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_auto_20170311_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='votos',
            field=models.IntegerField(default=0),
        ),
    ]
