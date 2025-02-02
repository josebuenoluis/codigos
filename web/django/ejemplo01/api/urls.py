from django.urls import path,include
from .views import TaskView,TaskViewXML

urlpatterns = [
    path('tasks/',TaskView.as_view(),name='task_list'),
    path('tasks/<int:pk>',TaskView.as_view(),name='una_task'),
    path('tasks/completadas/',TaskView.as_view(),name='completadas'),
    path('tasks_xml/',TaskViewXML.as_view(),name='tasks_xml'),
]