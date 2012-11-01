# -*- coding: utf-8 -*-
from django.contrib import admin
from projects.models import Project
from projects.models import Task

admin.site.register(Project)
admin.site.register(Task)
