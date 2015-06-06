# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_page_photourl'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Page',
            new_name='EventObject',
        ),
    ]
