from django.contrib import admin
from todoapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_complited', 'created_at','updated_at')
    search_fields = ('task',)
    
admin.site.register(Task, TaskAdmin)

# Register your models here.
