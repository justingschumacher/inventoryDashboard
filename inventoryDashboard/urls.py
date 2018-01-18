from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project/detail/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
]