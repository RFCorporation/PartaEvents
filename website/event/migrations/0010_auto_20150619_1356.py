# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20150616_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventobject',
            name='start_time',
            field=models.DateField(null=True, verbose_name=b'date', blank=True),
        ),
    ]
