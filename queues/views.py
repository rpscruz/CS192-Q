from django.shortcuts import render

from . models import Court, Venue, Match, Queue

from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)

class QueueListView(ListView):
    model = Queue
    template_name = 'queues/queues_list.html'
    context_object_name = 'queues_list'
    # ordering = ['venue']

class MatchCreateView(CreateView):
    model = Match
    fields = ['type', 'court', 'team1_p1', 'team2_p1', 'duration']
    success_url = '/queues/'

class MatchUpdateView(UpdateView):
    model = Match
    fields = ['type', 'court', 'team1_p1', 'team2_p1', 'duration']
    
    success_url = '/queues/'


class MatchDeleteView(DeleteView):
    model = Match #originally match
    success_url = '/queues/'

