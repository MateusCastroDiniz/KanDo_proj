from django.urls import path

from core.KanDo import views

#Assigns Board's view to home url.
urlpatterns = [
    path('', views.BoardView.as_view(), name='home')
]
