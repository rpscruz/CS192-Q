from django.shortcuts import render

from . models import Player

# from .forms import PlayerForm

from django.views.generic import (
	ListView, 
	CreateView,
	UpdateView,
	DeleteView
)

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