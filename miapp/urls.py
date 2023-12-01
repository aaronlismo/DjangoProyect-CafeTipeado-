
from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.index, name="index"),
    path('sobre/',views.sobre, name="sobre"),
    path('hola/<str:user>',views.hola, name="hola"),
    path('proyecto/',views.proyecto,name="proyecto"),
    path('tareas/',views.tareas,name="tareas"),
    path('crearTareas/',views.crear_tarea,name="crearTareas"),
    path('crearProyectos/',views.crear_proyecto,name="crearProyectos"),
    path('registro/',views.registro,name="registro"),
]