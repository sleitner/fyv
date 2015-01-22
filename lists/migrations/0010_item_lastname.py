# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_auto_20141105_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lastname',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
