# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('votes', models.CharField(max_length=100)),
                ('time', models.TimeField(auto_now_add=True, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
        ),
    ]
