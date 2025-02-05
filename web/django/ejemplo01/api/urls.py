from django.urls import path,include
from .views import TaskView,TaskViewXML
from rest_framework import routers  
from .views import TaskViewSet
from rest_framework.authtoken import views
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

router = routers.DefaultRouter()
router.register(r'tareas',TaskViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title= "Snippets API",
        default_version= 'v1',
        description= 'Test Description',
        terms_of_service= 'https://www.google.com/policies/terms/',
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('tasks/',TaskView.as_view(),name='task_list'),
    path('tasks/<int:pk>',TaskView.as_view(),name='una_task'),
    path('tasks/completadas/',TaskView.as_view(),name='completadas'),
    path('tasks_xml/',TaskViewXML.as_view(),name='tasks_xml'),
    path('',include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token),
    path('swagger<format>/',schema_view.without_ui(cache_timeout=0),name='schema-json'),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
]