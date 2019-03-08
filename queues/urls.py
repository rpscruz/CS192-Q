from django.urls import path
from .views import (
    QueueListView,
    MatchCreateView,
    MatchUpdateView,
    MatchDeleteView,
)

urlpatterns = [
    path('', QueueListView.as_view(), name='queues-list'),
    path('new/', MatchCreateView.as_view(), name='match-create'),
    path('update/<int:pk>/', MatchUpdateView.as_view(), name='match-update'),
    path('delete/<int:pk>/', MatchDeleteView.as_view(), name='match-delete'),
]
