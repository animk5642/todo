from django.urls import path
from . import views 


urlpatterns = [
   path('addTask/',views.addTask,name='addTask'),
   path('mark/<int:pk>/',views.markDone,name='mark'),
   path('delete/<int:pk>/',views.Delete,name="delete")
]