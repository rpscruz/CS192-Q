from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

#___________________________ACCOUNT VIEWS_____________________________
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#___________________________PLAYER VIEWS___________________________
class PlayerList(LoginRequiredMixin, ListView):
    model = Player
    ordering = ['first_name']
    template_name = 'queues/player/player_list.html'

    def get_queryset(self):
        return Player.objects.filter(user=self.request.user).order_by('first_name')

class PlayerView(LoginRequiredMixin, DetailView):
    model = Player
    template_name = 'queues/player/player_detail.html'

class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['last_name', 'first_name', 'player_level']
    success_url = reverse_lazy('player-list')
    template_name = 'queues/player/player_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlayerUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Player
    fields = ['last_name', 'first_name', 'player_level']
    success_url = reverse_lazy('player-list')
    template_name = 'queues/player/player_form.html'

    def test_func(self):
        player = self.get_object()
        if self.request.user == player.user:
            return True
        return False


class PlayerDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')
    template_name = 'queues/player/player_confirm_delete.html'
    
    def test_func(self):
        player = self.get_object()
        if self.request.user == player.user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.inQueue or self.object.inMatch:
            return HttpResponse("Player may be in a queue.")
        else:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)

#____________________________QUEUE VIEWS____________________________
class QueueView(LoginRequiredMixin, ListView):
    model = Queue
    ordering = ['created']
    template_name = 'queues/queues/queue_list.html'

    def get_queryset(self):
        return Queue.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(QueueView, self).get_context_data(**kwargs)
        onGoingQ = Queue.objects.filter(user=self.request.user, onGoing=True)
        inProgress = onGoingQ.exists()

        if inProgress:
            context['currentQ'] = onGoingQ[0]

        context['inProgress'] = inProgress
        context['queues'] = Queue.objects.filter(user=self.request.user, onGoing=False).order_by('-created')

        return context

class QueueDetail(LoginRequiredMixin, DetailView):
    model = Queue
    template_name = 'queues/queues/queue_detail.html'
    def get_context_data(self, **kwargs):
        context = super(QueueDetail, self).get_context_data(**kwargs)

        context['players'] = self.object.players.all()
        
        return context

class QueueCreate(LoginRequiredMixin, CreateView):
    model = Queue
    fields = ['match_type', 'court', 'players']
    success_url = reverse_lazy('queue-current')
    template_name = 'queues/queues/queue_form.html'

    def get_form(self, *args, **kwargs):
        form = super(QueueCreate, self).get_form(*args, **kwargs)
        form.fields['players'].queryset = Player.objects.filter(user=self.request.user)
        return form
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CurrentQView(LoginRequiredMixin, ListView):
    model = Queue
    template_name = 'queues/queues/currentQ_list.html' 
    
    def get_context_data(self, **kwargs):
        context = super(CurrentQView, self).get_context_data(**kwargs)
        onGoingQ = Queue.objects.filter(user=self.request.user, onGoing=True)
        inProgress = onGoingQ.exists()

        if inProgress:
            currentQ = onGoingQ[0]
            matches = currentQ.match_set.all()
            context['currentQ'] = currentQ
            context['players'] = currentQ.players.all()
            context['matches'] = matches.filter(user=self.request.user, queuedAt=currentQ, endDT=None).order_by('court_num')

        context['inProgress'] = inProgress

        return context

class CurrentQUpdatePlayer(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Queue
    fields = ['players']
    success_url = reverse_lazy('queue-current')
    template_name = 'queues/queues/queue_form.html'

    def get_form(self, *args, **kwargs):
        form = super(CurrentQUpdatePlayer, self).get_form(*args, **kwargs)
        form.fields['players'].queryset = Player.objects.filter(user=self.request.user)
        return form

    def test_func(self):
        queue = self.get_object()
        if self.request.user == queue.user:
            return True
        print("Fuckedt")
        return False
        

class CurrentQChangeCourt(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Queue
    fields = ['court']
    success_url = reverse_lazy('queue-current')
    template_name = 'queues/queues/queue_form.html'

    def test_func(self):
        queue = self.get_object()
        if self.request.user == queue.user:
            return True
        return False

class CurrentQEnd(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Queue
    fields = ['onGoing']
    success_url = reverse_lazy('queue-current')
    template_name = 'queues/queues/queue_form.html'

    def test_func(self):
        queue = self.get_object()
        if self.request.user == queue.user:
            return True
        return False

#____________________________MATCH VIEWS_____________________________
class MatchStartView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Match
    fields = ['umpire']
    success_url = reverse_lazy('queue-current')
    template_name = 'queues/match/match_form.html'

    def test_func(self):
        match = self.get_object()
        if self.request.user == match.user:
            return True
        return False

class SetWinnerView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Winner
    fields = ['players']
    success_url = reverse_lazy('queue-current')
    template_name = 'queues/match/winner_form.html'
    
    def test_func(self):
        match = self.get_object()
        if self.request.user == match.user:
            return True
        return False

    def get_form(self, *args, **kwargs):
        form = super(SetWinnerView, self).get_form(*args, **kwargs)
        form.fields['players'].queryset = self.object.match.players.all() 
        return form




