from django.urls import path
from .views import (
	QueueRecordView,
	QueueRecordCreateView,
	QueueRecordUpdateView,
)


urlpatterns = [
	path('', QueueRecordView.as_view(), name='queue-records'),
	path('records/', QueueRecordView.as_view(), name='queue-records'),
	path('records/new/', QueueRecordCreateView.as_view(), name='queue-records-create'),
	path('records/update/<int:pk>/', QueueRecordUpdateView.as_view(), name='queue-records-update'),

]