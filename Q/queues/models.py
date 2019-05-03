from django.db import models
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Player(models.Model):
	player_id = models.AutoField(primary_key=True)
	last_name = models.CharField(max_length=64, blank=False, null=True, verbose_name="Last Name")
	first_name = models.CharField(max_length=64, blank=False, null=True, verbose_name="First Name")
	player_level = models.PositiveSmallIntegerField(blank=False, default=0, null=True, verbose_name="Level")
	total_games = models.PositiveSmallIntegerField(blank=False, default=0, null=True, verbose_name="Game Count")
	total_wins = models.PositiveSmallIntegerField(blank=False, default=0, null=True, verbose_name="Total Wins")
	inQueue = models.BooleanField(blank=False, default=False, verbose_name="Currently in Queue")
	inMatch = models.BooleanField(blank=False, default=False, verbose_name="Currently in Match")

	def __str__(self):
		return self.first_name+' '+self.last_name
	
	class Meta:
		db_table = "player"
		unique_together=(
			('first_name', 'last_name'),
		)

class Queue(models.Model):
	MATCHTYPE_CHOICES = (
		('S', 'Singles'),
		('D', 'Doubles'),
	)
	queue_id = models.AutoField(primary_key=True)
	created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Date Created")
	match_type = models.CharField(max_length=1, choices=MATCHTYPE_CHOICES, default='S', blank=False, verbose_name="Match Type")
	court = models.PositiveSmallIntegerField(default=1, blank=False, validators=[MinValueValidator(1)], verbose_name="Number of Courts")
	players = models.ManyToManyField(Player, related_name='queues', verbose_name="Players in Queue")
	onGoing = models.BooleanField(blank=False, default=True, verbose_name="Queue in Progress")

	def __str__(self):
		formatedDate = self.created.strftime("%B %d, %Y %I:%M %p")
		return formatedDate
	
	def endQueue(self):
		qPlayers = self.players.all()
		for player in qPlayers:
			player.inQueue = False
			player.inMatch = False
			player.save()
	
	def clean(self):
		#______Handle endQueue_______
		if not self.onGoing:
			if self.match_set.filter(onGoing=True, endDT=None).exists():
				raise ValidationError('Matches are still on going.')

		#_______Handle change courts____________
		match = self.match_set.filter(onGoing=True)
		if self.court < match.count():
			raise ValidationError('Matches are ongoing in all courts.')

	def save(self, *args, **kwargs):
		try:
			temp = Queue.objects.get(onGoing=True)
			if self != temp:
				temp.onGoing = False
				temp.save()
			
		except Queue.DoesNotExist:
			pass
		super().save(*args,**kwargs)


class Match(models.Model):
	match_id = models.AutoField(primary_key=True)
	queuedAt = models.ForeignKey(Queue, on_delete=models.CASCADE, verbose_name="Queued at")
	startDT = models.DateTimeField(auto_now=False, auto_now_add=False, default=None, blank=True, null=True, verbose_name="Start Time")
	onGoing = models.BooleanField(blank=False, default=False, verbose_name="Match in Progress")
	endDT = models.DateTimeField(auto_now=False, auto_now_add=False, default=None, blank=True, null=True, verbose_name="End Time")
	players = models.ManyToManyField(Player, verbose_name="Players in Match")
	umpire = models.CharField(max_length=64, blank=False, default=None, null=True, verbose_name="Umpire")
	court_num = models.PositiveSmallIntegerField(default=1, null=True, validators=[MinValueValidator(1)], verbose_name="Court ID")

	def getWinner(self):
		try:
			return self.winner.winner_id
		except ObjectDoesNotExist:
			print("Winner does not exist")






class Winner(models.Model):
	winner_id = models.AutoField(primary_key=True)
	match = models.OneToOneField(Match, on_delete=models.CASCADE, blank=False)
	players = models.ManyToManyField(Player)

	




		
		




