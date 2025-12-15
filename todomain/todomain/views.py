from django.shortcuts import render
from todoapp.models import Task
def home(request):
    task =  Task.objects.filter(is_complited =False)

    task2 = {
    'mytask':task
    }

    return render(request,'home.html',task2)

