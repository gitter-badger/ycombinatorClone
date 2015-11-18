# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0004_forum_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='counter',
            field=models.CharField(max_length=100),
        ),
    ]
