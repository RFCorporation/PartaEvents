# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20150602_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=300)),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'date', blank=True)),
                ('owner_name', models.CharField(default=b'', max_length=200)),
                ('place', models.CharField(default=b'', max_length=200)),
                ('category', models.CharField(default=b'', max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='AddUrl',
            new_name='Url',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
