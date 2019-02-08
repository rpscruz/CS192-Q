from django.urls import path
from .views import (
	QueueRecordView,
	QueueRecordCreateView,
	QueueRecordUpdateView,
	CourtListView,
	CourtCreateView,
	CourtDeleteView,
)


urlpatterns = [
	path('records/', QueueRecordView.as_view(), name='queue-records'),
	path('records/new/', QueueRecordCreateView.as_view(), name='queue-records-create'),
	path('records/update/<int:pk>/', QueueRecordUpdateView.as_view(), name='queue-records-update'),
	path('', CourtListView.as_view(), name='queue-court'),
	path('addcourt/', CourtCreateView.as_view(), name='court-create'),
	path('/court/<int:pk>/delete/', CourtDeleteView.as_view(), name='court-delete'),

]