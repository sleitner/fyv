# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('zipcode', models.IntegerField(default=None, null=True)),
                ('list', models.ForeignKey(default=None, to='lists.List')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lastname', models.CharField(default='', null=True, max_length=100)),
                ('firstname', models.CharField(default='', null=True, max_length=100)),
                ('middlename', models.CharField(default='', null=True, max_length=100)),
                ('suffix', models.CharField(default='', null=True, max_length=3)),
                ('city', models.CharField(default='', null=True, max_length=100)),
                ('zip', models.IntegerField(default='0', null=True)),
                ('zip4', models.IntegerField(default='0', null=True)),
                ('DOB', models.IntegerField(default='0', null=True)),
                ('gender', models.CharField(default='', max_length=3)),
                ('party', models.CharField(default='', max_length=100)),
                ('countycode', models.IntegerField(default='0', null=True)),
                ('legdistrict', models.IntegerField(default='0', null=True)),
                ('towncity', models.CharField(default='', null=True, max_length=100)),
                ('ward', models.IntegerField(default='0', null=True)),
                ('congressdistrict', models.IntegerField(default='0', null=True)),
                ('lastvote', models.IntegerField(default='0', null=True)),
                ('regdate', models.IntegerField(default='0', null=True)),
                ('P1993', models.IntegerField(default='0')),
                ('P1994', models.IntegerField(default='0')),
                ('P1995', models.IntegerField(default='0')),
                ('P1996', models.IntegerField(default='0')),
                ('P1997', models.IntegerField(default='0')),
                ('P1998', models.IntegerField(default='0')),
                ('P1999', models.IntegerField(default='0')),
                ('P2000', models.IntegerField(default='0')),
                ('P2001', models.IntegerField(default='0')),
                ('P2002', models.IntegerField(default='0')),
                ('P2003', models.IntegerField(default='0')),
                ('P2004', models.IntegerField(default='0')),
                ('P2005', models.IntegerField(default='0')),
                ('P2006', models.IntegerField(default='0')),
                ('P2007', models.IntegerField(default='0')),
                ('P2008', models.IntegerField(default='0')),
                ('P2009', models.IntegerField(default='0')),
                ('P2010', models.IntegerField(default='0')),
                ('P2011', models.IntegerField(default='0')),
                ('P2012', models.IntegerField(default='0')),
                ('P2013', models.IntegerField(default='0')),
                ('P2014', models.IntegerField(default='0')),
                ('G1992', models.IntegerField(default='0')),
                ('G1993', models.IntegerField(default='0')),
                ('G1994', models.IntegerField(default='0')),
                ('G1995', models.IntegerField(default='0')),
                ('G1996', models.IntegerField(default='0')),
                ('G1997', models.IntegerField(default='0')),
                ('G1998', models.IntegerField(default='0')),
                ('G1999', models.IntegerField(default='0')),
                ('G2000', models.IntegerField(default='0')),
                ('G2001', models.IntegerField(default='0')),
                ('G2002', models.IntegerField(default='0')),
                ('G2003', models.IntegerField(default='0')),
                ('G2004', models.IntegerField(default='0')),
                ('G2005', models.IntegerField(default='0')),
                ('G2006', models.IntegerField(default='0')),
                ('G2007', models.IntegerField(default='0')),
                ('G2008', models.IntegerField(default='0')),
                ('G2009', models.IntegerField(default='0')),
                ('G2010', models.IntegerField(default='0')),
                ('G2011', models.IntegerField(default='0')),
                ('G2012', models.IntegerField(default='0')),
                ('G2013', models.IntegerField(default='0')),
                ('G2014', models.IntegerField(default='0')),
                ('nyid', models.IntegerField(default='0')),
                ('prob', models.FloatField(default='-1.0')),
                ('list', models.ForeignKey(default=None, to='lists.List')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
