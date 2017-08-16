# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20170813_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(3, '故障'), (4, '备用'), (1, '在线'), (2, '已下线')], default=1, null=True, verbose_name='资产状态'),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(3, '故障'), (4, '备用'), (1, '在线'), (2, '已下线')], default=1, verbose_name='资产状态'),
        ),
    ]