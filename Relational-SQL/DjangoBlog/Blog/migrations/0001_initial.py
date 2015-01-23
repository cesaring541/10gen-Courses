# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('comment_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('publication_date', models.DateField()),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('comment_id', models.ManyToManyField(to='Blog.Comment', db_table=b'post_comments')),
            ],
            options={
                'db_table': 'posts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='tag_id',
            field=models.ManyToManyField(to='Blog.Tag', db_table=b'post_tags'),
            preserve_default=True,
        ),
    ]
