# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20170302_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'time created'),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'time updated'),
        ),
    ]