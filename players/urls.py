from django.urls import path
from .views import (
	PlayerListView,
	PlayerCreateView,
	PlayerUpdateView,
	PlayerDeleteView,
)

urlpatterns = [
    path('', PlayerListView.as_view(), name='players-list'),
    path('new/', PlayerCreateView.as_view(), name='players-create'),
    path('update/<int:pk>/', PlayerUpdateView.as_view(), name='players-update'),
    path('delete/<int:pk>/', PlayerDeleteView.as_view(), name='players-delete'),
]
