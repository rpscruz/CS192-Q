# Generated by Django 2.1.5 on 2019-04-28 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0020_auto_20190428_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winner',
            old_name='player',
            new_name='players',
        ),
    ]
