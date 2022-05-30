from django.urls import path
from . import views

urlpatterns = [
    path('smart/notes', views.NotesView.as_view(), name='note.list'),
    path('smart/notes/create', views.NotesCreateView.as_view(), name='note.create'),
]
