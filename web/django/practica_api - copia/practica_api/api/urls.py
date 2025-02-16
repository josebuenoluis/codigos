from django.urls import path,include
from .views import ProyectosView,JefeProyectoView,ProyectosViewSet,JefeProyectoViewSet,ProyectosViewXML,JefeProyectosViewXML
from rest_framework import routers
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r"setproyectos",ProyectosViewSet)  
router.register(r"setjefes",JefeProyectoViewSet)

urlpatterns = [
    path('proyectos/',ProyectosView.as_view(),name="proyectos_list"),
    path("jefes/",JefeProyectoView.as_view(),name='jefes_list'),
    path('proyectos/<int:pk>',ProyectosView.as_view(),name='proyecto_get'),
    path('jefes/<str:dni>',JefeProyectoView.as_view(),name='jefe_get'),
    path('proyectos_xml/',ProyectosViewXML.as_view(),name="proyectos_list_xml"),
    path('jefes_xml/',JefeProyectosViewXML.as_view(),name="jefeproyectos_list_xml"),
    path('',include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token),
]