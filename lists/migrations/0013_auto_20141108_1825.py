# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0012_auto_20141108_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(max_length=100, default='templast'),
            preserve_default=True,
        ),
    ]
