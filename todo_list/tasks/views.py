from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from tasks.forms import TaskForm, TaskFilterForm
from tasks.models import Task


@login_required
def task_list(request):
    """Все задачи."""
    form = TaskFilterForm(request.GET)
    tasks = Task.objects.all()

    if form.is_valid() and form.cleaned_data['status']:
        tasks = tasks.filter(status=form.cleaned_data['status'])

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})


@login_required
def task_create(request):
    """Создание новой задачи."""
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form = form.save()
        form.save()
        return redirect('tasks:task_list')

    return render(request, 'tasks/task_create.html', {'form': form})


@login_required
def task_update(request, pk):
    """Изменение выбранной задачи."""
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('tasks:task_list')
    
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'tasks/task_create.html', context=context)


@login_required
def task_delete(request, pk):
    """Удаление выбранной задачи."""
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')

    return render(request, 'tasks/task_delete.html', {'task': task})
