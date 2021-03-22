from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255, unique=True)
    project_date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


class Data(models.Model):
    year = 'Y'
    FIELD = [
        (year, 'ежегодные данные'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=1, choices=FIELD)
    data = models.TextField()
    begin_heating = models.DateField()
    end_heating = models.DateField()
