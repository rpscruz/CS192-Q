from django.shortcuts import render, render_to_response, HttpResponseRedirect

from . models import Player

# from .forms import PlayerForm

from django.views.generic import (
	ListView, 
	CreateView,
	UpdateView,
	DeleteView
)

# from django.db.models import ProtectedError
from django.db import IntegrityError
from django.http import HttpResponse

class PlayerListView(ListView):
	model = Player
	template_name = 'players/playerslist.html'
	context_object_name = 'player_list'
	ordering = ['last_name']

class PlayerCreateView(CreateView):
	model = Player
	fields = ['first_name', 'last_name', 'player_level']

class PlayerUpdateView(UpdateView):
	model = Player
	fields = ['first_name', 'last_name', 'player_level']

class PlayerDeleteView(DeleteView):
    model = Player
    success_url = '/players/'

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
            # return self.delete(request, *args, **kwargs)
        except IntegrityError:
            return render_to_response('players/player_in_queue.html')

            # return HttpResponse(template.render(context, request))