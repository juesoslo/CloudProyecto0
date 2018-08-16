# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-16 16:08
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0008_merge_20180816_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evento.Categoria'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_final',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 16, 16, 8, 31, 199840), null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 16, 16, 8, 31, 199804), null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_registro',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 16, 16, 8, 31, 199906), null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='evento.Usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]