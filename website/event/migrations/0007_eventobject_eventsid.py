# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20150606_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventobject',
            name='eventsID',
            field=models.IntegerField(default=0),
        ),
    ]
