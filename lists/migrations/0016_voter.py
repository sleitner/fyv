# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0015_auto_20141109_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('firstname', models.CharField(max_length=100, default='')),
                ('lastname', models.CharField(max_length=100, default='')),
                ('byr', models.IntegerField(default='0')),
                ('list', models.ForeignKey(to='lists.List', default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
