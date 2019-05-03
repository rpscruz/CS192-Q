from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from . models import Player, Queue, Match, Winner
from . filters import MatchFilter

import django_filters


#___________________________TEMPLATE VIEWS___________________________
class HomePageView(TemplateView):

    template_name = "queues/home.html"


#___________________________PLAYER VIEWS___________________________
class PlayerList(ListView):
    model = Player
    ordering = ['last_name']

class PlayerView(DetailView):
    model = Player

class PlayerCreate(CreateView):
    model = Player
    fields = ['last_name', 'first_name', 'player_level']
    success_url = reverse_lazy('player-list')

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['last_name', 'first_name', 'player_level']
    success_url = reverse_lazy('player-list')

class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.inQueue or self.object.inMatch:
            return HttpResponse("Player may be in a queue.")
        else:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)

#____________________________QUEUE VIEWS____________________________
class QueueView(ListView):
    model = Queue
    ordering = ['created']
    template_name = 'queues/queue_list.html'

    def get_context_data(self, **kwargs):
        context = super(QueueView, self).get_context_data(**kwargs)
        onGoingQ = Queue.objects.filter(onGoing=True)
        inProgress = onGoingQ.exists()

        if inProgress:
            context['currentQ'] = onGoingQ[0]

        context['inProgress'] = inProgress
        context['queues'] = Queue.objects.filter(onGoing=False).order_by('-created')

        return context

class QueueDetail(DetailView):
    model = Queue

    def get_context_data(self, **kwargs):
        context = super(QueueDetail, self).get_context_data(**kwargs)

        context['players'] = self.object.players.all()
        
        return context

class QueueCreate(CreateView):
    model = Queue
    fields = ['match_type', 'court', 'players']
    success_url = reverse_lazy('queue-current')


class CurrentQView(ListView):
    model = Queue
    template_name = 'queues/currentQ_list.html' 
    
    def get_context_data(self, **kwargs):
        context = super(CurrentQView, self).get_context_data(**kwargs)
        onGoingQ = Queue.objects.filter(onGoing=True)
        inProgress = onGoingQ.exists()

        if inProgress:
            currentQ = onGoingQ[0]
            matches = currentQ.match_set.all()
            context['currentQ'] = currentQ
            context['players'] = currentQ.players.all()
            context['matches'] = matches.filter(queuedAt=currentQ, endDT=None).order_by('court_num')

        context['inProgress'] = inProgress

        return context

class CurrentQUpdatePlayer(UpdateView):
    model = Queue
    fields = ['players']
    success_url = reverse_lazy('queue-current')

        

class CurrentQChangeCourt(UpdateView):
    model = Queue
    fields = ['court']
    success_url = reverse_lazy('queue-current')

class CurrentQEnd(UpdateView):
    model = Queue
    fields = ['onGoing']
    success_url = reverse_lazy('queue-current')

#____________________________MATCH VIEWS_____________________________
class MatchStartView(UpdateView):
    model = Match
    fields = ['umpire']
    success_url = reverse_lazy('queue-current')


class SetWinnerView(UpdateView):
    model = Winner
    fields = ['players']
    success_url = reverse_lazy('queue-current')

    def get_form(self, *args, **kwargs):
        form = super(SetWinnerView, self).get_form(*args, **kwargs)
        form.fields['players'].queryset = self.object.match.players.all() 
        return form

#____________________________MATCH VIEWS_____________________________


# class RecordView(ListView):
#     model = Match
#     ordering = ['queuedAt', 'court_num']
#     filterset_class = MatchFilter
#     template_name = 'queues/match_list.html'
    
#     def get_context_data(self, **kwargs):
#         context = super(RecordView, self).get_context_data(**kwargs)
#         context['filter'] = MatchFilter

#         return context



