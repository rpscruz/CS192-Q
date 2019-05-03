from django.urls import path
from . import views

urlpatterns = [
    path('', views.QueueView.as_view(), name='queue-list'),
    #___Current Queue Links___
    path('current/', views.CurrentQView.as_view(), name='queue-current'),
    path('edit/<int:pk>', views.CurrentQUpdatePlayer.as_view(), name='queue-editPlayer'),
    path('end/<int:pk>', views.CurrentQEnd.as_view(), name='queue-currentEnd'),
    path('courts/<int:pk>', views.CurrentQChangeCourt.as_view(), name='queue-editCourts'),
    #___General Queue Links___
    path('view/<int:pk>', views.QueueDetail.as_view(), name='queue-view'),
    path('new/', views.QueueCreate.as_view(), name='queue-new'),
    # path('delete/<int:pk>', views.PlayerDelete.as_view(), name='player-delete'),
]