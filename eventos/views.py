from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .forms import EventoForm, PersonaForm, TipoForm
from eventos.models import Evento, Inscripcion, Persona, TipoEvento
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def lista_eventos(request):
    eventos = Evento.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'eventos/evento_list.html', {'eventos':eventos})
@login_required
def evento_detalle(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/evento_detalle.html', {'evento': evento})
@login_required
def evento_editar(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/evento_editar.html', {'form': form})
@login_required
def evento_eliminar(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    evento.delete()
    return redirect('lista_eventos')
@login_required
def evento_nuevo(request):
    if request.method == "POST":
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            evento = Evento.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion=formulario.cleaned_data['descripcion'], fecha=formulario.cleaned_data['fecha'], tipo=formulario.cleaned_data['tipo'])
            for persona_id in request.POST.getlist('personas'):
                inscripcion = Inscripcion(persona_id=persona_id, evento_id = evento.id)
                inscripcion.save()
            messages.add_message(request, messages.SUCCESS, 'Evento guardado exitosamente')
    else:
        formulario = EventoForm()
    return render(request, 'eventos/evento_nuevo.html', {'formulario': formulario})
@login_required
def lista_personas(request):
    personas = Persona.objects.order_by('id')
    return render(request, 'personas/persona_list.html', {'personas':personas})
@login_required
def persona_nueva(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/persona_nueva.html', {'form': form})
@login_required
def persona_detalle(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'personas/persona_detalle.html', {'persona': persona})
@login_required
def persona_editar(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'personas/persona_editar.html', {'form': form})
@login_required
def persona_eliminar(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    persona.delete()
    return redirect('lista_personas')
@login_required
def lista_tipo(request):
    tipos = TipoEvento.objects.order_by('id')
    return render(request, 'tipos/tipo_list.html', {'tipos':tipos})
@login_required
def tipo_nuevo(request):
    if request.method == "POST":
        form = TipoForm(request.POST)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect('lista_tipo')
    else:
        form = TipoForm()
    return render(request, 'tipos/tipo_nuevo.html', {'form': form})
@login_required
def tipo_detalle(request, pk):
    tipo = get_object_or_404(TipoEvento, pk=pk)
    return render(request, 'tipos/tipo_detalle.html', {'tipo': tipo})
@login_required
def tipo_editar(request, pk):
    tipo = get_object_or_404(TipoEvento, pk=pk)
    if request.method == "POST":
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect('lista_tipo')
    else:
        form = TipoForm(instance=tipo)
    return render(request, 'tipos/tipo_editar.html', {'form': form})
@login_required
def tipo_eliminar(request, pk):
    tipo = get_object_or_404(TipoEvento, pk=pk)
    tipo.delete()
    return redirect('lista_tipo')
