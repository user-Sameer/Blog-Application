# Generated by Django 3.1.4 on 2022-01-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='comments',
            field=models.IntegerField(),
        ),
    ]
