# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owners',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
