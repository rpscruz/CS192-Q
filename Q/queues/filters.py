from . models import Match
import django_filters

class MatchFilter(django_filters.FilterSet):
    class Meta:
        model = Match
        fields = ['queuedAt', 'court_num', 'umpire', 'players']