"""Readable URL names make links independent of URL text."""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("tasks/new/", views.task_form, name="task_add"),
    path("tasks/<int:pk>/edit/", views.task_form, name="task_edit"),
    path("tasks/<int:pk>/complete/", views.complete_task, name="task_complete"),
    path("tasks/<int:pk>/delete/", views.delete_task, name="task_delete"),
]
