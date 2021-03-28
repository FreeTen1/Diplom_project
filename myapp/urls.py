from django.urls import path
from .views import IndexView, ProjectData, ProjectCreate

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:pk>', ProjectData.as_view()),
    path('create_project', ProjectCreate.as_view()),
]