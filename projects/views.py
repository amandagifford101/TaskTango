from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

# Create your views here.


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_receipt = form.save(False)
            new_receipt.purchaser = request.user
            new_receipt.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)


def delete_project(request, id):
    projects = get_object_or_404(Project, id=id)
    context = {
        "projects": projects,
    }
    if request.method == "POST":
        projects_delete = Project.objects.get(id=id)
        projects_delete.delete()
        return redirect("list_projects")
    return render(request, "projects/delete.html", context)
