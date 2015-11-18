# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0002_forum_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='linka',
            field=models.CharField(default=datetime.datetime(2015, 11, 18, 15, 19, 56, 695848, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forum',
            name='linkb',
            field=models.CharField(default=datetime.datetime(2015, 11, 18, 15, 20, 3, 943978, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
