# Generated by Django 2.1.5 on 2019-02-08 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0003_auto_20190207_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_type', models.CharField(choices=[('S', 'Single'), ('D', 'Doubles')], default='S', max_length=2)),
                ('isFree', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='matchrecord',
            name='queue_rec',
        ),
        migrations.DeleteModel(
            name='MatchRecord',
        ),
    ]