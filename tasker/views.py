import logging
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .models import TaskState
from .forms import TaskForm

logger = logging.getLogger('tasker.' + __name__)


@login_required
def new_task(request):

    if request.method == 'POST':
        form_task = TaskForm(request.POST)
        if form_task.is_valid():
            new_task = form_task.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            logger.debug("Created new task id: %d", new_task.id)
            return redirect('/')
    else:
        form_task = TaskForm()

    return render(request, 'tasker/new_task.html', {'form_task': form_task})


class TaskListView(LoginRequiredMixin, generic.ListView):
    template_name = 'tasker/list_tasks.html'
    context_object_name = 'list_tasks'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-create_date')


class TaskView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = 'tasker/info_task.html'
