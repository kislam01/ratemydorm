# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20170305_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='floor',
            field=models.CharField(choices=[(b'Basement', b'Basement'), (b'First', b'First'), (b'Second', b'Second'), (b'Third', b'Third'), (b'Fourth', b'Fourth'), (b'Fifth', b'Fifth')], default=b'First', max_length=10),
        ),
    ]
