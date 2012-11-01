# -*- coding: utf-8 -*-

from django.views.generic import ListView
from projects.models import Task
from projects.models import Project
class ProjectsView(ListView):

    template_name="projects/projects-list.html"
    model = Project
