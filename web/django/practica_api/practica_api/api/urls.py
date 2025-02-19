from django.urls import path,include
<<<<<<< HEAD
from .views import ProyectosViewSet,JefeProyectoViewSet
from rest_framework import routers
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r"proyectos",ProyectosViewSet)  
router.register(r"jefes",JefeProyectoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token),
=======
from .views import UsuariosView


urlpatterns = [
    path('usuarios/',UsuariosView.as_view(),name="usuarios_list")
>>>>>>> 1f322e2f831b8d0a1d643f6dc4d20b325f0186a3
]