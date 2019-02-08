from django.db import models
from django.urls import reverse

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=100)
	level = models.PositiveSmallIntegerField()
	total_games = models.PositiveSmallIntegerField(default=0, editable=False)
	total_wins = models.PositiveSmallIntegerField(default=0, editable=False)
	#on_queue = models.BooleanField(default=False)
	#in_match = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('players-list')
