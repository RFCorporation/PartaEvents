# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_eventobject_eventsid'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventobject',
            name='description',
            field=models.CharField(default=b'', max_length=2000),
        ),
    ]
