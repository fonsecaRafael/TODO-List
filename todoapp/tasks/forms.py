from django.forms import ModelForm

from todoapp.tasks.models import Tasks


class NewTaskForm(ModelForm):

    class Meta:
        model = Tasks
        fields = ['name']
