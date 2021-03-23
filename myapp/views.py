from django.views.generic import ListView, DetailView

from django.shortcuts import render
from django.contrib.auth.models import User

from myapp.models import Project, Data


class IndexView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a_projects'] = Project.objects.filter(user__username=self.request.user)
        return context


class ProjectData(DetailView):
    model = Data
    template_name = 'index.html'
    context_object_name = 'single_project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a_projects'] = Project.objects.filter(user__username=self.request.user)
        return context
