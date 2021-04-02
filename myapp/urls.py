from django.urls import path
from .views import IndexView, ProjectData, ProjectCreate, ProjectDelete

urlpatterns = [
    path('', IndexView.as_view()),
    path('projects/<int:pk>', ProjectData.as_view()),
    path('create_project', ProjectCreate.as_view()),
    path('delete/<int:pk>', ProjectDelete.as_view()),
]