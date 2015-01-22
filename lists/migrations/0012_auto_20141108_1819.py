# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0011_auto_20141108_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('list', models.ForeignKey(to='lists.List', default=None)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
