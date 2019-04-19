from django import forms
from project_app.models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name','describle','status']
        widgets = {
            'status': forms.RadioSelect()
        }