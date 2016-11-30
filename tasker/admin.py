from django.contrib import admin

from .models import Task, TaskState
# Register your models here.

@admin.register(TaskState)
class TaskStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
