from django.urls import path

from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project'),
    path('<slug>/', ProjectDetailView.as_view(), name='project-details')
]