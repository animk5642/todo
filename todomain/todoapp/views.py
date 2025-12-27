from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Task
# Create your views here.


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def markDone(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        raise Http404("Item not found.") #else we can add get_object_or_404
    task.is_complited=True
    task.save()

    return redirect('home')
    return HttpResponse(task)

def Delete(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        raise Http404("Item not found.") #else we can add get_object_or_404
    Task.objects.filter(pk=pk).delete()
    return redirect('home')    
