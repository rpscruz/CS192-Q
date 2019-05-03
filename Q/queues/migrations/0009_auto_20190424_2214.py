# Generated by Django 2.1.5 on 2019-04-24 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0008_remove_player_match_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='players',
        ),
        migrations.RemoveField(
            model_name='match',
            name='queuedAt',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='match',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='player',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='Winner',
        ),
    ]