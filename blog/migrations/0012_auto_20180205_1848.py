# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-05 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.FileField(default='settings.STATIC_ROOT/media/images/courseone.jpg', upload_to=''),
        ),
    ]
