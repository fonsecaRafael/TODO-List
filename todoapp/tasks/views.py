from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from todoapp.tasks.forms import NewTaskForm, TaskForm
from todoapp.tasks.models import Tasks


def home(request):
    pending_tasks = Tasks.objects.filter(done=False).all()
    done_tasks = Tasks.objects.filter(done=True).all()
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:home'))
        else:
            return render(request, 'tasks/home.html',
                          {
                              'form': form,
                              'pending_tasks': pending_tasks,
                              'done_tasks': done_tasks
                          },
                          status=400)
    return render(request, 'tasks/home.html',
                  {
                      'pending_tasks': pending_tasks,
                      'done_tasks': done_tasks
                  })


def detail(request, task_id):
    task = Tasks.objects.get(id=task_id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('tasks:home'))
