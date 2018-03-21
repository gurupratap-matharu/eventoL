# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-21 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20180316_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='event_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='manager.EventUser', verbose_name='Event User'),
            preserve_default=False,
        ),
    ]
