from django.urls import path
from .views import (
    VenueListView,
    VenueCreateView,
    VenueUpdateView,
    VenueDeleteView,
)

urlpatterns = [
    path('', VenueListView.as_view(), name='venues-list'),
    path('new/', VenueCreateView.as_view(), name='venues-create'),
    path('update/<int:pk>/', VenueUpdateView.as_view(), name='venues-update'),
    path('delete/<int:pk>/', VenueDeleteView.as_view(), name='venues-delete'),
]
