# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0010_item_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='lastname',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
