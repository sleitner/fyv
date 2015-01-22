# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_list_shared_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.CharField(max_length=32, default=''),
            preserve_default=True,
        ),
    ]
