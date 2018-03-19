# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20170305_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four'), (5, b'Five')], default=3),
        ),
    ]
