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
    template_name = 'project_details.html'
    context_object_name = 'single_project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data = Data.objects.get(id=self.kwargs.get('pk'))
        # Блок создания словаря с ежемесячными данными в шаблонизатор
        list_data = list(map(float, data.data.split(' ')))
        months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        context['output_data'] = {}
        for number, month in zip(list_data, months):
            context['output_data'][month] = number
        # Конец блока

        context['coef'] = data.coef
        context['a_project'] = Data.objects.filter(project__user__username=self.request.user)
        context['list_data'] = list_data  # сухие данные
        return context

    def post(self, request, *args, **kwargs):
        editable_data = Data.objects.get(id=self.kwargs.get('pk')) # данные которые менять

        monthly_data = ' '.join([request.POST['Январь'], request.POST['Февраль'], request.POST['Март'], request.POST['Апрель'], request.POST['Май'], request.POST['Июнь'], request.POST['Июль'], request.POST['Август'], request.POST['Сентябрь'], request.POST['Октябрь'], request.POST['Ноябрь'], request.POST['Декабрь']]) # создание строки с данными
        begin_heating = request.POST.get('begin_heating', False) # начало отоп
        end_heating = request.POST.get('end_heating', False) # конец отоп
        coef = request.POST['coef']

        # Блок обновления данных
        editable_data.data = monthly_data
        editable_data.begin_heating = begin_heating
        editable_data.end_heating = end_heating
        editable_data.coef = coef
        # конец блока

        editable_data.save()
        return super().get(request, *args, **kwargs)


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
class ProjectUpdate(ListView):
    model = Data
    template_name = 'create_project.html'
    form_class = CreateProjectForm

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=self.kwargs.get('pk'))
        project.project_name = request.POST['project_name']
        project.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a_project'] = Data.objects.filter(project__user__username=self.request.user)
        context['project_name'] = Data.objects.get(project__id=self.kwargs.get('pk')).project.project_name
        return context


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
