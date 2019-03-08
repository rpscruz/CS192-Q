from django.shortcuts import render

# Create your views here.
from . models import Court, Venue, Match, Record

from django.views.generic import (
    ListView, 
    DeleteView
)

class RecordListView(ListView):
    model = Record 
    template_name = 'records/records_list.html'
    context_object_name = 'records_list'
    # ordering = ['venue']

class RecordDeleteView(DeleteView):
    model = Record #originally match
    success_url = '/records/'

