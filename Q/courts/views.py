from django.shortcuts import render

from . models import Court, Venue

from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)

class CourtListView(ListView):
    model = Court
    template_name = 'courts/courts_list.html'
    context_object_name = 'courts_list'
    ordering = ['venue', 'court_name']

class CourtCreateView(CreateView):
    model = Court
    fields = ['court_name', 'venue']


class CourtUpdateView(UpdateView):
    model = Court
    fields = ['court_name', 'venue']

class CourtDeleteView(DeleteView):
    model = Court
    success_url = '/courts/'

