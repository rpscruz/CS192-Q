from django.urls import path
from django_filters.views import FilterView
from . filters import MatchFilter
from . models import Match

urlpatterns = [
    path('', FilterView.as_view(model=Match, filterset_class=MatchFilter, template_name = 'queues/match/match_list.html'), name='record-list'),
]