# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0014_auto_20141108_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='text',
            new_name='firstname',
        ),
    ]
