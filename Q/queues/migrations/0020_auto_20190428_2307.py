# Generated by Django 2.1.5 on 2019-04-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0019_auto_20190427_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='onGoing',
            field=models.BooleanField(default=False, verbose_name='Match in Progress'),
        ),
    ]
