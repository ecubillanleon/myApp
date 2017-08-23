# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_pub', models.DateField()),
                ('encabezado', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reportero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_completo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='reportero',
            field=models.ForeignKey(to='miapp.Reportero'),
        ),
    ]
