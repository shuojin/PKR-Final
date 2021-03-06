# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pkr_user', '0007_auto_20171204_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRecord', models.DateField()),
                ('quantity', models.IntegerField()),
                ('customerNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pkr_user.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='officeCode',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='reportsTo',
        ),
        migrations.AddField(
            model_name='product',
            name='customerNumber',
            field=models.ForeignKey(default=b'', null=True, on_delete=django.db.models.deletion.CASCADE, to='pkr_user.Customer'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('customerNumber', 'productCode')]),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Office',
        ),
        migrations.AddField(
            model_name='stock',
            name='productCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pkr_user.Product'),
        ),
    ]
