from django.db import models
from django.urls import reverse
from django.utils.timezone import now



# Create your models here.

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=100, blank=False, null=True)
    creation_date = models.DateTimeField(default=now, blank=False)

    class Meta:
        managed = False
        db_table = 'venue'

    def __str__(self):
        return self.venue_name

    def get_absolute_url(self):
        return reverse('venues-list')
