# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-13 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_final',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
