from django.urls import path
from .views import NoteListView, NoteDetailView

urlpatterns = [
    path('', NoteListView.as_view(), name='note'),
    path('<slug>/', NoteDetailView.as_view(), name='note-details'),
]