# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_remove_review_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'uploads/'),
        ),
    ]