from django.views.generic import ListView

from django.shortcuts import render
from django.contrib.auth.models import User

from myapp.models import Project, Data


class IndexView(ListView):
    model = Project
    template_name = 'index.html'

