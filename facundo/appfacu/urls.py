from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('estudiantes/crear', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:idalum>', views.editar_estudiante, name='editar_estudiante'), 
    path('estudiantes/borrar/<int:idalum>', views.borrar_estudiante, name='borrar_estudiante'),   
    path('usuarios', views.usuarios, name='usuarios'),
]
