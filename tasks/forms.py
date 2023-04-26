from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
            "is_completed",
        )

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control-sm"}),
            "start_date": forms.DateInput(
                attrs={"class": "form-control-sm"},
            ),
            "due_date": forms.DateInput(
                attrs={"class": "form-control-sm"},
            ),
            "project": forms.Select(attrs={"class": "form-control-sm"}),
            "assignee": forms.Select(attrs={"class": "form-control-sm"}),
            "is_completed": forms.CheckboxInput(),
        }


class TaskSpecificForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
            "is_completed",
        )

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control-sm"}),
            "start_date": forms.DateInput(
                attrs={"class": "form-control-sm"},
            ),
            "due_date": forms.DateInput(
                attrs={"class": "form-control-sm"},
            ),
            "project": forms.TextInput(
                attrs={"class": "form-control-sm", "readonly": "readonly"}
            ),
            "assignee": forms.Select(attrs={"class": "form-control-sm"}),
            "is_completed": forms.CheckboxInput(),
        }
