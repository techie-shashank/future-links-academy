# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20180105_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ManyToManyField(to='tests.Question')),
            ],
        ),
    ]
