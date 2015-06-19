# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20150619_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventobject',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name=b'date', blank=True),
        ),
    ]
