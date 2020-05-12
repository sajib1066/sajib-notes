from django.urls import path
from .views import NoteDetailView

urlpatterns = [
    path('<slug>/', NoteDetailView.as_view(), name='note-details'),
]