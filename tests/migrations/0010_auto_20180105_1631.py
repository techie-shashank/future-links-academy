# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choices',
            name='id',
        ),
        migrations.RemoveField(
            model_name='choices',
            name='option',
        ),
        migrations.AddField(
            model_name='choices',
            name='four',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choices',
            name='one',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choices',
            name='right_answer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='choices',
            name='selected_option',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='choices',
            name='three',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choices',
            name='two',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='choices',
            name='question',
        ),
        migrations.AddField(
            model_name='choices',
            name='question',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tests.Question'),
            preserve_default=False,
        ),
    ]
