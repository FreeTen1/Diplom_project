from django.views.generic import ListView

from django.shortcuts import render
from django.contrib.auth.models import User

from myapp.models import Project, Data


class TestView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'
    queryset = Project.objects.all()

