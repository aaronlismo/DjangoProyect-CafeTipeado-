from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse,JsonResponse
from .models import Proyecto,Tareas
from .form import CrearNuevaTarea,CrearNuevoProyecto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.

def registro(request):

    if request.method == 'GET':
        return render(request,'Login/Registro.html',
        {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
           try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('index')
           except IntegrityError:
               return render(request,'Login/Registro.html',
                {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                })
        else:
             return render(request,'Login/Registro.html',
                {
                    'form': UserCreationForm,
                    'error': "Contraseña no coincidente"
                })


def index(request):
    titulo = "Café Tipeado"
    return render(request,'index.html',{
        'titulo': titulo
    })

def hola(request,user):
    return HttpResponse("<h1>Hola Mundo , %s ya estoy aprendiendo con Django</h1>" % user)

def sobre(request):
    titulo = "Café Tipeado"
    return render(request,'sobre.html',
                  {
                      'titulo': titulo
                  })

def proyecto(request):
    # proyectos = list(Proyecto.objects.values())
    proyectos = Proyecto.objects.all()
    titulo = "Café Tipeado"
    return render(request,'proyectos/Proyectos.html',
                  {
                      'proyectos':proyectos,
                      'titulo': titulo
                  })

def tareas(request):
    # tareas = get_object_or_404(Tareas,id=id)
    tareas = Tareas.objects.all()
    titulo = "Café Tipeado"
    return render(request,'tareas/Tareas.html',{
        'tareas': tareas,
        'titulo': titulo
    })

def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'tareas/CrearTarea.html',
                  {
                      'form':CrearNuevaTarea
                  })
    else:
        Tareas.objects.create(titulo=request.POST['titulo'],descripcion=request.POST['descripcion'],proyecto_id=1)
        return redirect('tareas')
    
def crear_proyecto(request):
    if request.method == 'GET':
        return render(request,'proyectos/CrearProyecto.html',
                  {
                      'form':CrearNuevoProyecto
                  })
    else:
        Proyecto.objects.create(name=request.POST['name'])
        return redirect('proyecto')