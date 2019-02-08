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

class Court(models.Model):
	COURT_TYPE_CHOICES = (
		('S', 'Single'),
		('D', 'Doubles'),
	)

	court_type = models.CharField(max_length=2, choices=COURT_TYPE_CHOICES, default='S')
	isFree = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse('queue-court')


# class MatchRecord(models.Model):
# 	queue_rec = models.ForeignKey(QueueRecord, on_delete=models.CASCADE)
# 	court_num = models.PositiveSmallIntegerField()
# 	umpire = models.CharField(max_length=100)
# 	match_duration = models.DurationField()
# 	score = models.CharField(max_length=100)
# 	winners = models.CharField(max_length=200)
# 	losers = models.CharField(max_length=200)


# 	def __str__(self):
# 		return self.id