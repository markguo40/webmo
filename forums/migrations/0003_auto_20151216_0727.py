# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 07:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20151216_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='forum',
            new_name='session',
        ),
    ]
