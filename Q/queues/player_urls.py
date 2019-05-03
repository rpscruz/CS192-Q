from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerList.as_view(), name='player-list'),
    path('view/<int:pk>', views.PlayerView.as_view(), name='player-view'),
    path('new/', views.PlayerCreate.as_view(), name='player-new'),
    path('edit/<int:pk>', views.PlayerUpdate.as_view(), name='player-edit'),
    path('delete/<int:pk>', views.PlayerDelete.as_view(), name='player-delete'),
]