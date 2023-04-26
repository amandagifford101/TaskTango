from django import forms
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control-sm"}),
            "description": forms.TextInput(attrs={"class": "form-control-sm"}),
            "owner": forms.Select(attrs={"class": "form-control-sm"}),
        }
