from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm, TaskSpecificForm


# Create your views here.
def show_project(request, id):
    projects = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    remaining = Task.objects.filter(
        assignee=request.user, project=id, is_completed=False
    )
    progress = Task.objects.filter(
        assignee=request.user, project=id, is_completed=True
    )
    progress_count = progress.count()
    remaining_count = remaining.count()
    total_count = progress_count + remaining_count
    if total_count > 0:
        progress_percentage = int(progress_count / total_count * 100)
        remaining_percentage = int(remaining_count / total_count * 100)
    else:
        progress_percentage = 0
        remaining_percentage = 100
    task = Task.objects.filter(assignee=request.user, project=id)
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "project": project,
        "projects": projects,
        "task": task,
        "tasks": tasks,
        "remaining_count": remaining_count,
        "progress_count": progress_count,
        "progress_percentage": progress_percentage,
        "remaining_percentage": remaining_percentage,
    }
    return render(request, "tasks/project_tasks.html", context)


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
def create_task_specific(request, id):
    projects = get_object_or_404(Project, id=id)
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
        "projects": projects,
    }
    return render(request, "tasks/create_specific.html", context)


# The button on the create_task_specific page from project list is not working and no specific task is being created
# Will need to restore TaskForm to TaskSpecificForm if want to test again


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/mine.html", context)


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        "task": task,
    }
    if request.method == "POST":
        tasks_delete = Task.objects.get(id=id)
        tasks_delete.delete()
        return redirect("show_my_tasks")
    return render(request, "tasks/delete.html", context)
