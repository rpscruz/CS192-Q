from django.db import models
from django.urls import reverse

# Create your models here.
class QueueRecord(models.Model):
     queue_date = models.DateTimeField(auto_now_add=True)
     court_count = models.PositiveSmallIntegerField()
     on_going = models.BooleanField(default=True)

     def __str__(self):
          return self.queue_date

     def get_absolute_url(self):
          return reverse('queue-records')

class QueuePlayer(models.Model):
     queue_rec    = models.ForeignKey(QueueRecord, on_delete=models.CASCADE)
     player       = models.ManyToManyField('players.Player')
     games_played = models.PositiveSmallIntegerField(default=0)
     games_won    = models.PositiveSmallIntegerField(default=0)

class Court(models.Model):
     court_name = models.CharField(max_length=100)

     
class QueueCourt(models.Model):
     queue_rec = models.ForeignKey(QueueRecord, on_delete=models.CASCADE)
     isFree    = models.BooleanField(default=True)

class MatchRecord(models.Model):
     queue_rec = models.ForeignKey(QueueRecord, on_delete=models.CASCADE)
     court_num = models.PositiveSmallIntegerField()
     umpire    = models.CharField(max_length=100)
     match_duration = models.DurationField()
     score     = models.CharField(max_length=100)
     winners   = models.CharField(max_length=200)
     losers    = models.CharField(max_length=200)


     def __str__(self):
          return self.id