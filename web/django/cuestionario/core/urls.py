from django.urls import path
from core import views as core_views

urlpatterns = [
    path('',core_views.home,name="home"),
    path('galeria',core_views.galeria,name="galeria"),
]