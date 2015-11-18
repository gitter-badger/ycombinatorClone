# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0005_auto_20151118_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='counter',
            field=models.IntegerField(),
        ),
    ]
