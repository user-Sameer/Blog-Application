# Generated by Django 3.1.4 on 2022-01-14 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000000)),
                ('tags', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('comments', models.IntegerField(max_length=10000)),
                ('author', models.CharField(max_length=1000)),
            ],
        ),
    ]
