# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkr_user', '0004_auto_20171204_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productScale',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
