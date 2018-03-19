# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20170305_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='competetiveness',
            field=models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')], default=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='floor',
            field=models.CharField(choices=[(b'B', b'BASEMENT'), (b'First', b'FIRST'), (b'Second', b'SECOND'), (b'Third', b'THIRD'), (b'Fourth', b'FOURTH'), (b'Fifth', b'FIFTH')], default=b'first', max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='handicap_rating',
            field=models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')], default=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')], default=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='room_type',
            field=models.CharField(choices=[(b'Single', b'SINGLE'), (b'Double', b'DOUBLE'), (b'Triple', b'TRIPLE'), (b'Suite', b'SUITE')], default=b'Single', max_length=10),
        ),
    ]
