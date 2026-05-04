from django.shortcuts import render, redirect
from .models import Task 
from .forms import TaskForm

def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()    
    
    all_tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': all_tasks, 'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')