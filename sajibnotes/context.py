from django.db.models import Count
from notes import models as notemodel
from project import models as projectmodel

def note_context(request):
    note_category = notemodel.Category.objects.all()
    note_tag = notemodel.Tag.objects.all()
    popular_note = notemodel.Note.objects.filter(is_delete=False).order_by('-id')[:3]

    context = {
        'note_ctg': note_category,
        'note_tag': note_tag,
        'popular_note': popular_note,
    }
    return context

def project_context(request):
    project_category = projectmodel.Category.objects.all().annotate(number_of_project=Count('project')).order_by('-number_of_project', 'name')
    project_tag = projectmodel.Tag.objects.all()
    popular_project = projectmodel.Project.objects.filter(is_delete=False).order_by('-id')[:3]

    print('Project Category: ', project_category)

    context = {
        'project_ctg': project_category,
        'project_tag': project_tag,
        'popular_project': popular_project
    }
    return context