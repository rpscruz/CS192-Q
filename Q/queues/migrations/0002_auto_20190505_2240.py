# Generated by Django 2.1.5 on 2019-05-05 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='user',
        ),
        migrations.RemoveField(
            model_name='player',
            name='user',
        ),
        migrations.RemoveField(
            model_name='queue',
            name='user',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='user',
        ),
    ]
