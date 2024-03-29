# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-06-14 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_material', '0003_auto_20200608_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousYearPapers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.PositiveSmallIntegerField(choices=[(1, b'Science'), (2, b'Maths'), (4, b'Chemistry'), (3, b'Physics')])),
                ('standard', models.PositiveSmallIntegerField(choices=[(9, b'Class 9'), (10, b'Class 10'), (11, b'Class 11'), (12, b'Class 12')])),
                ('year', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to='media/')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='previousyearpapers',
            unique_together=set([('subject', 'standard', 'year')]),
        ),
    ]
