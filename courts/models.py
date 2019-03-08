from django.db import models
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=100, blank=false, null=True)
    creation_date = models.DateTimeField(default=now, blank=false)

    def __str__(self):
        return self.venue_name

    class Meta:
        managed = False
        db_table = 'venue'

class Court(models.Model):
    court_id = models.AutoField(primary_key=True)
    court_name = models.CharField(max_length=100, blank=false, null=True)
    venue = models.ForeignKey('Venue', models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now, blank=false)

    class Meta:
        managed = False
        db_table = 'court'

    def __str__(self):
        return self.court_name

    def get_absolute_url(self):
        return reverse('courts-list')

