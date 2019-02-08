from django.shortcuts import render
from django.http import HttpResponse

from . models import QueueRecord, QueueCourt

from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
)

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

# court
class QueueCourtView(ListView):
	model = QueueCourt
	context_object_name = 'queue_courts'
	ordering = ['queue_rec']


# class MatchRecordView(ListView):
# 	model = MatchRecord
# 	context_object_name = 'match_records'
# 	ordering = ['queue_rec'

