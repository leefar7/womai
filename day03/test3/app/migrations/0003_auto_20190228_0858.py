# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-28 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190227_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='i_person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Person'),
        ),
    ]
