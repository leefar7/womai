# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('typeid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('typename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'womai_shop',
            },
        ),
    ]
