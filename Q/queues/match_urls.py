from django.urls import path
from . import views

urlpatterns = [
    path('start/<int:pk>', views.MatchStartView.as_view(), name='match-start'),
    path('end/<int:pk>', views.SetWinnerView.as_view(), name='match-end'),
    
    # path('', views.QueueView.as_view(), name='queue-list'),
    #___Current Queue Links___
    # path('current/', views.CurrentQView.as_view(), name='queue-current'),
    # path('edit/<int:pk>', views.CurrentQUpdatePlayer.as_view(), name='queue-editPlayer'),
    #___General Queue Links___
    # path('view/<int:pk>', views.QueueDetail.as_view(), name='queue-view'),
    # path('new/', views.QueueCreate.as_view(), name='queue-new'),
    # # path('delete/<int:pk>', views.PlayerDelete.as_view(), name='player-delete'),
]