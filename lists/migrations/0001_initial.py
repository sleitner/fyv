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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('firstname', models.CharField(max_length=100, default='')),
                ('lastname', models.CharField(max_length=100, default='')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('lastname', models.CharField(max_length=100, default='', null=True)),
                ('firstname', models.CharField(max_length=100, default='', null=True)),
                ('middlename', models.CharField(max_length=100, default='', null=True)),
                ('suffix', models.CharField(max_length=3, default='', null=True)),
                ('city', models.CharField(max_length=100, default='', null=True)),
                ('zip', models.IntegerField(default='0', null=True)),
                ('zip4', models.IntegerField(default='0', null=True)),
                ('DOB', models.IntegerField(default='0', null=True)),
                ('gender', models.CharField(max_length=3, default='')),
                ('party', models.CharField(max_length=100, default='')),
                ('countycode', models.IntegerField(default='0', null=True)),
                ('legdistrict', models.IntegerField(default='0', null=True)),
                ('towncity', models.CharField(max_length=100, default='', null=True)),
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
