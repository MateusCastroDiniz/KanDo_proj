from django.urls import path

from core.KanDo import views

urlpatterns = [
    path('', views.BoardView.as_view(), name='home')
]
