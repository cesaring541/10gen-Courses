# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_permalink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
