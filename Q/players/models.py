from django.db import models
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.

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
        unique_together = ['last_name', 'first_name']

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('players-list')
