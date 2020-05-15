from django.urls import path
from .views import NoteListView, NoteDetailView, note_details

urlpatterns = [
    path('', NoteListView.as_view(), name='note'),
    # path('<slug>/', NoteDetailView.as_view(), name='note-details'),
    path('<slug>/', note_details, name='note-details'),
]