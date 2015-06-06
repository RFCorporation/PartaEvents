# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20150606_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='photoUrl',
            field=models.URLField(default=b'', max_length=500),
        ),
    ]
