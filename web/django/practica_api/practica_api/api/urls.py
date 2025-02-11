from django.urls import path,include
from .views import UsuariosView


urlpatterns = [
    path('usuarios/',UsuariosView.as_view(),name="usuarios_list")
]