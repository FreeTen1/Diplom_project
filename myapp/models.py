# Выпускная работа бакалавра
# студентки группы А-12-17
# Торчкова Михаила Васильевича

# Листинг модуля "models.py" приложения "myapp"

# ==========

# Импортируемые модули
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# класс, созданный по таблице Project
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255, unique=True)
    project_date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.project_name} | {self.user}"


# класс, созданный по таблице Data
class Data(models.Model):
    month = 'M'
    FIELD = [
        (month, 'ежемесячные данные'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=1, choices=FIELD, default='M')
    data = models.TextField(default='0 0 0 0 0 0 0 0 0 0 0 0')
    begin_heating = models.DateField(default=f'{datetime.now().year - 1}-10-15')
    end_heating = models.DateField(default=f'{datetime.now().year}-04-15')
    coef = models.FloatField(default=1.1)

    def __str__(self):
        return f'{self.id} данные проекта "{self.project}"'
