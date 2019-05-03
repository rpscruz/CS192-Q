from django.urls import path
from django_filters.views import FilterView
from . filters import MatchFilter
from . models import Match

urlpatterns = [
    path('', FilterView.as_view(model=Match, filterset_class=MatchFilter, template_name = 'queues/match_list.html'), name='record-list'),
    #___Current Queue Links___
    # path('current/', views.CurrentQView.as_view(), name='queue-current'),
    # path('edit/<int:pk>', views.CurrentQUpdatePlayer.as_view(), name='queue-editPlayer'),
    # path('end/<int:pk>', views.CurrentQEnd.as_view(), name='queue-currentEnd'),
    # path('courts/<int:pk>', views.CurrentQChangeCourt.as_view(), name='queue-editCourts'),
    #___General Queue Links___
    # path('view/<int:pk>', views.QueueDetail.as_view(), name='queue-view'),
    # path('new/', views.QueueCreate.as_view(), name='queue-new'),
    # path('delete/<int:pk>', views.PlayerDelete.as_view(), name='player-delete'),
]