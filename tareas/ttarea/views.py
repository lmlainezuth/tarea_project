# ttarea/views.py
from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()

    tareas = Tarea.objects.all()
    return render(request, 'ttarea/lista_tareas.html', {'tareas': tareas, 'form': form})

def home(request):
    return render(request, 'ttarea/home.html')