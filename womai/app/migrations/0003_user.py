# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(default='axf.png', max_length=100)),
                ('rank', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'womai_user',
            },
        ),
    ]