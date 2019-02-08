# Generated by Django 2.1.5 on 2019-02-06 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatchRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_num', models.PositiveSmallIntegerField()),
                ('umpire', models.CharField(max_length=100)),
                ('match_duration', models.DurationField()),
                ('score', models.CharField(max_length=100)),
                ('winners', models.CharField(max_length=200)),
                ('losers', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QueueRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue_date', models.DateTimeField(auto_now_add=True)),
                ('court_count', models.PositiveSmallIntegerField()),
                ('on_going', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='matchrecord',
            name='queue_rec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queues.QueueRecord'),
        ),
    ]
