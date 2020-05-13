from django.shortcuts import render
from django.views.generic import ListView

from .models import Project

class ProjectListView(ListView):
    queryset = Project.objects.filter(is_delete=False)
    template_name = 'project/project.html'
