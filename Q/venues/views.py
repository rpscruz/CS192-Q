from django.shortcuts import render

from . models import Venue

from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)

class VenueListView(ListView):
    model = Venue
    template_name = 'venues/venues_list.html'
    context_object_name = 'venues_list'
    ordering = ['venue_name']

class VenueCreateView(CreateView):
    model = Venue
    fields = ['venue_name']

class VenueUpdateView(UpdateView):
    model = Venue
    fields = ['venue_name']

class VenueDeleteView(DeleteView):
    model = Venue
    success_url = '/venues/'