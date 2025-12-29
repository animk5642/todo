from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Task
# Create your views here.


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def markDone(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        raise Http404("Item not found.")  # else we can add get_object_or_404
    task.is_complited = True
    task.save()

    return redirect('home')
    return HttpResponse(task)


def undone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_complited = False
    task.save()
    # Task.objects.create(task=task)
    # Task.objects.filter(pk=pk).delete()
    return redirect('home')


def Delete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        raise Http404("Item not found.")  # else we can add get_object_or_404
    task.delete()
    return redirect('home')


def edit_task(request, pk):

    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        content = {

            'mytask': task,
        }

        return render(request, 'edit.html', content)
