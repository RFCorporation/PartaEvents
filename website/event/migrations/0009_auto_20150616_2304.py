# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_eventobject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventobject',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='eventobject',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]
