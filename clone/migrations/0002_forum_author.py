# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='author',
            field=models.CharField(max_length=100, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
