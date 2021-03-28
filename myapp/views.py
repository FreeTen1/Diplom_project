from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from myapp.forms import CreateProjectForm
from myapp.models import Project, Data


class IndexView(ListView):
    model = Data
    template_name = 'index.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a_project'] = Data.objects.filter(project__user__username=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class ProjectData(DetailView):
    model = Data
    template_name = 'index.html'
    context_object_name = 'single_project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a_project'] = Data.objects.filter(project__user__username=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class ProjectCreate(CreateView):
    template_name = 'create_project.html'
    form_class = CreateProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a_project'] = Data.objects.filter(project__user__username=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        project_name = request.POST['project_name']

        project = Project(user=self.request.user, project_name=project_name)
        project.save()

        data_project = Data(project=project)
        data_project.save()
        return super().get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ProjectDelete(DeleteView):
    model = Project
    template_name = 'delete_project.html'
    queryset = Project.objects.all()
    success_url = '/'
    context_object_name = 'single_project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a_project'] = Data.objects.filter(project__user__username=self.request.user)
        return context
