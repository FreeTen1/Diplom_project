from django.urls import path
from .views import IndexView, ProjectData

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:pk>', ProjectData.as_view()),
]