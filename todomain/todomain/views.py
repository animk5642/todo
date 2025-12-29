from django.shortcuts import render
from todoapp.models import Task
def home(request):
    task =  Task.objects.filter(is_complited =False).order_by('-updated_at')
    complited_task = Task.objects.filter(is_complited =True).order_by('-updated_at')
    tasks = {
    'mytask':task,
    'complited':complited_task
    }
 

    return render(request,'home.html',tasks)

