from django import forms

from tasks.models import Task, STATUS_CHOICES


class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(choices=STATUS_CHOICES)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'status')
