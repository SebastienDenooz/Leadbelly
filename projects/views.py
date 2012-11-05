# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from projects.models import Task
from projects.models import Project
from projects.forms import ProjectForm

class ProjectsView(ListView):

    template_name="projects/projects-list.html"
    model = Project

class ProjectCreateView(CreateView):
    form_class = ProjectForm
    success_url  = reverse_lazy('projects-list')

    def form_invalid(self, form):
        # Attention les erreurs du form ne seront pas affichées
        return HttpResponseRedirect(self.success_url)