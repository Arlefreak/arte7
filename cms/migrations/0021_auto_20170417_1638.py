# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_auto_20170417_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrasesHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.CharField(editable=False, max_length=200)),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name': 'Frase del home',
                'verbose_name_plural': 'Frases del home',
                'ordering': ['order'],
            },
        ),
        migrations.AlterField(
            model_name='personal',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
