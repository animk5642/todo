from django.urls import path
from . import views 


urlpatterns = [
   path('addTask/',views.addTask,name='addTask'),
   path('mark/<int:pk>/',views.markDone,name='mark'),
   path('delete/<int:pk>/',views.Delete,name="delete"),
   #mark as undone
   path('undone/<int:pk>',views.undone, name='undone'),

   #edit feature
   path('edit_task/<int:pk>',views.edit_task,name ='edit')
   
]