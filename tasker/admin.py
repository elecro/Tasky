from django.contrib import admin

from .models import Task, TaskState
# Register your models here.

@admin.register(TaskState)
class TaskStateAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'state')
    list_filter = ('state',)
