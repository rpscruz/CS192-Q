# Generated by Django 2.1.5 on 2019-02-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='total_games',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='total_wins',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
