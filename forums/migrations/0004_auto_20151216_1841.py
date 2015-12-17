# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_auto_20151216_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='urlname',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
