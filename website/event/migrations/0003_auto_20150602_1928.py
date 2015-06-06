# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_addurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='owner_name',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='place',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name=b'date', blank=True),
        ),
        migrations.AlterField(
            model_name='addurl',
            name='url',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=b'', max_length=300),
        ),
    ]
