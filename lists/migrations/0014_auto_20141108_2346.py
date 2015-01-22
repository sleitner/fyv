# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0013_auto_20141108_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
