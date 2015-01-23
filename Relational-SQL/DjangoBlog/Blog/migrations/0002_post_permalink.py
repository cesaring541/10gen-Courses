# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='permalink',
            field=models.CharField(default=b'Not Found', max_length=200),
            preserve_default=True,
        ),
    ]
