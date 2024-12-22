from django.shortcuts import render,redirect,get_object_or_404
from .todo_forms import TaskCreationForm
from .models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def task_list(req):
    tasks = Task.objects.filter(user=req.user).order_by('-created_at')
    return render(req, 'todo_app/task_list.html', {'tasks': tasks})


@login_required
def add_task(req):
    if req.method == 'POST':
        form = TaskCreationForm(req.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = req.user
            task.save()
            return redirect('task_listing')
    else:
        form = TaskCreationForm()
    return render(req, 'todo_app/task_form.html', {'form': form})


@login_required
def update_task(req,task_id):
    task = get_object_or_404(Task, id=task_id, user=req.user)
    if req.method == 'POST':
        form = TaskCreationForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_listing')
    else:
        form = TaskCreationForm(instance=task)
    return render(req, 'todo_app/task_form.html', {'form': form})


@login_required
def delete_task(req, task_id):
    task = get_object_or_404(Task, id=task_id, user=req.user)
    task.delete()
    return redirect('task_listing')
    
