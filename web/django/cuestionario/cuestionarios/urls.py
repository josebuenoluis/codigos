from django.urls import path
from cuestionarios import views as cuestionarios_views

urlpatterns = [
    path('',cuestionarios_views.cuestionarios,name="cuestionarios"),
    path('crear',cuestionarios_views.crear_cuestionario,name="crear_cuestionario"),
]