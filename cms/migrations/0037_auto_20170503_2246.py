# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0036_auto_20170503_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='title',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]