# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 05:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='BlogsPost',
        ),
    ]
