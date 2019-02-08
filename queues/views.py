from django.shortcuts import render
from django.http import HttpResponse

from . models import QueueRecord
from . models import Court

from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
)

#_____________QUEUERECORD________________#
class QueueRecordView(ListView):
	model = QueueRecord
	context_object_name = 'queue_records'
	ordering = ['queue_date']

class QueueRecordCreateView(CreateView):
	model = QueueRecord
	fields = ['court_count']

class QueueRecordUpdateView(UpdateView):
	model = QueueRecord
	fields = ['on_going']
#________________________________________#

#_________________COURTS_________________#

class CourtListView(ListView):
	model = Court
	context_object_name = 'queue_courts'

class CourtCreateView(CreateView):
	model = Court
	fields = ['court_type']

class CourtDeleteView(DeleteView):
 	model = Court
 	success_url = '/queues/'
#________________________________________#

# class MatchRecordView(ListView):
# 	model = MatchRecord
# 	context_object_name = 'match_records'
# 	ordering = ['queue_rec']

