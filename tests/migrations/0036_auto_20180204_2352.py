# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-04 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0035_remove_score_wrong_questions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-marks']},
        ),
        migrations.RemoveField(
            model_name='question',
            name='option4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_no',
        ),
    ]
