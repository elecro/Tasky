from django.conf.urls import url

from . import views

app_name = 'tasker'
urlpatterns = [
    url(r'^new/$', views.new_task, name="new_task"),
    url(r'^list/$', views.TaskListView.as_view(), name="list_tasks"),
    url(r'^$', views.TaskListView.as_view(), name="list_tasks_base"),
    url(r'^view/(?P<pk>[0-9]+)/$', views.TaskView.as_view(), name="view_task"),
]
