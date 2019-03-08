from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils import timezone

import datetime


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    first_name = models.CharField(max_length=100, blank=False, null=True)
    player_level = models.SmallIntegerField(blank=False, null=True)
    total_games = models.SmallIntegerField(default=0, null=True)
    total_win = models.SmallIntegerField(default=0, null=True)
    creation_date = models.DateTimeField(default=now, blank=True)

    class Meta:
        managed = False
        db_table = 'player'

    def __str__(self):
        return self.first_name+' '+self.last_name

    def get_absolute_url(self):
        return reverse('players-list')

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=100, blank=False, null=True)
    creation_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.venue_name

    class Meta:
        managed = False
        db_table = 'venue'

class Court(models.Model):
    court_id = models.AutoField(primary_key=True)
    court_name = models.CharField(max_length=100, blank=False, null=True)
    venue = models.ForeignKey('Venue', models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now, blank=True)

    class Meta:
        managed = False
        db_table = 'court'

    def __str__(self):
        return str(self.venue)+' '+str(self.court_name)

    def get_absolute_url(self):
        return reverse('court-list')

class MatchType(models.Model):
    mt_id = models.SmallIntegerField(primary_key=True)
    type = models.CharField(max_length=7, blank=False, null=True)

    def __str__(self):
        return self.type

    class Meta:
        managed = False
        db_table = 'match_type'

class Match(models.Model):
    m_id = models.AutoField(primary_key=True)
    type = models.ForeignKey('MatchType', models.DO_NOTHING, db_column='type', blank=False, null=True)
    
    # first players of each team
    team1_p1 = models.ForeignKey('Player', models.DO_NOTHING, related_name='team1_p1', db_column='team1_p1', null=True)
    team2_p1 = models.ForeignKey('Player', models.DO_NOTHING, related_name='team2_p1', db_column='team2_p1', null=True)
    
    # second players of each team
    team1_p2 = models.ForeignKey('Player', models.DO_NOTHING, related_name='team1_p2', db_column='team1_p2', null=True)
    team2_p2 = models.ForeignKey('Player', models.DO_NOTHING, related_name='team2_p2', db_column='team2_p2', null=True)
 
    court = models.ForeignKey('Court', models.DO_NOTHING)
    creation_date = models.DateTimeField(default=timezone.now(), blank=False)
    duration = models.DurationField(null=False, blank=False, default='01:00:00')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'match'

    def get_absolute_url(self):
        return reverse('queues_list')

    
# https://zxq9.com/archives/616
class Queue(models.Model):
    m_id = models.SmallIntegerField(blank=True,  primary_key=True)

    type = models.ForeignKey('MatchType', models.DO_NOTHING, db_column='type', blank=False, null=True)

    # first players of each team
    team1_p1 = models.ForeignKey('Player', models.DO_NOTHING, related_name='q_team1_p1', db_column='team1_p1', null=True)
    team2_p1 = models.ForeignKey('Player', models.DO_NOTHING, related_name='q_team2_p1', db_column='team2_p1', null=True)
    
    # second players of each team
    team1_p2 = models.ForeignKey('Player', models.DO_NOTHING, related_name='q_team1_p2', db_column='team1_p2', null=True)
    team2_p2 = models.ForeignKey('Player', models.DO_NOTHING, related_name='q_team2_p2', db_column='team2_p2', null=True)
    court = models.ForeignKey('Court', models.DO_NOTHING)
    creation_date = models.DateTimeField(default=timezone.now(), blank=False)
    duration = models.DurationField(null=False, blank=False, default='01:00:00')  # This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'queue'

    def get_absolute_url(self):
        return reverse('queues_list')


    @property    
    def remaining_time(self):

        diff = ( datetime.datetime.now() - self.creation_date )
        self.duration = self.duration - diff
        total_seconds_x = int(self.duration.total_seconds())
        hours = int(total_seconds_x / 3600)
        minutes = int((total_seconds_x % 3600) / 60)




        # return self.duration
        return self.duration


