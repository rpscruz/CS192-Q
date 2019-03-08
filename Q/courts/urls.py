from django.urls import path
from .views import (
    CourtListView,
    CourtCreateView,
    CourtUpdateView,
    CourtDeleteView,
)

urlpatterns = [
    path('', CourtListView.as_view(), name='courts-list'),
    path('new/', CourtCreateView.as_view(), name='court-create'),
    path('update/<int:pk>/', CourtUpdateView.as_view(), name='court-update'),
    path('delete/<int:pk>/', CourtDeleteView.as_view(), name='court-delete'),
]
