# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-19 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'make_description_a_text_field'),
    ]

    operations = [
        migrations.DeleteModel(
            name='T',
        ),
    ]
