from django.shortcuts import render
from projects.models import Project


# Create your views here.
def show_project(request, id):
    projects = Project.objects.get(id=id)
    context = {
        "projects": projects,
    }
    return render(request, "tasks/show_project.html", context)
