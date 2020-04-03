from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='rooms'),
    path('room', views.room, name='room'),
    path('search', views.search, name='search'),
]