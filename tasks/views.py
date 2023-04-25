from django.shortcuts import render, redirect
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


# Create your views here.
def show_project(request, id):
    projects = Project.objects.get(id=id)
    context = {
        "projects": projects,
    }
    return render(request, "tasks/show_project.html", context)


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            new_task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/mine.html", context)
