# Generated by Django 3.1.4 on 2022-01-14 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220114_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='comment',
            new_name='comments',
        ),
    ]
