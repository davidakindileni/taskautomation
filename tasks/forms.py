"""Use Django's ModelForm to validate input before saving it."""
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "frequency", "next_due_date"]
        widgets = {
            "next_due_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "description": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_title(self):
        # Reject titles made only of spaces.
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("Enter a task title.")
        return title
