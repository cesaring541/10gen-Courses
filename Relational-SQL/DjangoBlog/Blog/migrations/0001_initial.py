# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'authors',
            },
            bases=(models.Model,),
        ),
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
                ('author_id', models.ForeignKey(to='Blog.Author', db_column=b'author_id')),
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
