# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20170305_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='floor',
            field=models.CharField(choices=[(b'B', b'Basement'), (b'first', b'First'), (b'second', b'Second'), (b'third', b'Third'), (b'fourth', b'Fourth'), (b'fifth', b'Fifth')], default=b'first', max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='room_type',
            field=models.CharField(choices=[(b'single', b'Single'), (b'double', b'Double'), (b'triple', b'Triple'), (b'suite', b'Suite')], default=b'single', max_length=10),
        ),
    ]