from django.urls import path
from .views import (
    RecordListView,
    RecordDeleteView,
)

urlpatterns = [
    path('', RecordListView.as_view(), name='records-list'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='records-delete'),
]
