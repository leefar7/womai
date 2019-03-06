# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-01 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190228_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=40)),
                ('sex', models.BooleanField()),
            ],
        ),
    ]
