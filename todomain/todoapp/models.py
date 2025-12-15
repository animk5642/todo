from django.db import models

# Create your models here.evey model we created should be registerd okk dont forget register in admin


class Task(models.Model):
  task =  models.CharField(max_length=250)
  is_complited = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
         return self.task
  
  
  
  




