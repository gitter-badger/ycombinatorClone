# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0003_auto_20151118_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='counter',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
