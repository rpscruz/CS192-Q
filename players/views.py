from django.shortcuts import render

from . models import Player

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
	ordering = ['name']

class PlayerCreateView(CreateView):
	model = Player
	fields = ['name', 'level']

class PlayerUpdateView(UpdateView):
	model = Player
	fields = ['name', 'level']

class PlayerDeleteView(DeleteView):
 	model = Player
 	success_url = '/players/'