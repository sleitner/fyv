# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_auto_20141105_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([]),
        ),
    ]
