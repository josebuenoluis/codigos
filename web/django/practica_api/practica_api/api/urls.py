from django.urls import path,include
from .views import ProyectosViewSet,JefeProyectoViewSet
from rest_framework import routers
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r"proyectos",ProyectosViewSet)  
router.register(r"jefes",JefeProyectoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token),
]