from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project

class ProjectListView(ListView):
    queryset = Project.objects.filter(is_delete=False)
    template_name = 'project/project.html'

class ProjectDetailView(DetailView):
    queryset = Project.objects.filter(is_delete=False)
    template_name = 'project/details.html'
