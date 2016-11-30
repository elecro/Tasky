from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class TaskState(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    description = models.TextField()
    state = models.ForeignKey(TaskState)
