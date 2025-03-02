from django.urls import path
from estadisticas import views as estadisticas_views

urlpatterns = [
    path('',estadisticas_views.estadisticas,name="estadisticas"),
]