from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Alumnos, Usuarios

from .forms import EstudianteForm

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def estudiantes(request):
    estudiantes = Alumnos.objects.all()
    return render(request, 'estudiantes/estudiantes.html', {'estudiantes':estudiantes})

def crear_estudiante(request):
    formulario = EstudianteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        #print(formulario)
        formulario.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/crear.html', {'formulario': formulario})

def editar_estudiante(request, idalum):
    estudiante = Alumnos.objects.get(idalum=idalum)
    formulario = EstudianteForm(request.POST or None, request.FILES or None, instance=estudiante)
    if formulario.is_valid() and request.method=='POST':
        formulario.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/editar.html', {'formulario': formulario})

def borrar_estudiante(request, idalum):
    estudiante = Alumnos.objects.get(idalum=idalum)
    estudiante.delete()
    return redirect('estudiantes')

def usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios':usuarios})