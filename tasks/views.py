from django.shortcuts import render
from .models import Task 

def task_list(request):
    all_tasks = Task.objects.all()
    
    return render(request, 'tasks/list.html', {'tasks': all_tasks})