# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-01 21:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0093_non_null_size_in_instance_status_history_entries'),
    ]

    operations = [
        migrations.AddField(
            model_name='instancestatushistory',
            name='extra',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
