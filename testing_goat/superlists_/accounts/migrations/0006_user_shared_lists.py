# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_auto_20170329_0851'),
        ('accounts', '0005_auto_20170216_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shared_lists',
            field=models.ManyToManyField(related_name='shared_with', to='lists.List'),
        ),
    ]
