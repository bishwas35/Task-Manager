from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        if title:
            Task.objects.create(title=title)
    return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
    return redirect('index')
