from django.shortcuts import render, render_to_response, get_object_or_404
from .models import *

def carrera(request, slug=None):
    list = PlanDeEstudios.objects.all()
    if slug:
        single = get_object_or_404(PlanDeEstudios, slug = slug)
    else:
        single = PlanDeEstudios.objects.all().first()

    for item in list:
        if item.slug == single.slug:
            item.active = True

    context = {
        'list': list,
        'single': single
    }
    return render(request, 'carrera_de_cine.html', context)

def cursos(request, curso_slug=None, temario_slug=None):
    list_cursos = CursosTalleres.objects.all()
    if curso_slug:
        single_curso = get_object_or_404(CursosTalleres, slug = curso_slug)
    else:
        single_curso = CursosTalleres.objects.all().first()

    for item in list_cursos:
        if item.slug == single_curso.slug:
            item.active = True

    list_temarios = Temario.objects.filter(curso=single_curso)
    print(temario_slug)
    print(curso_slug)
    if temario_slug:
        single_temario = get_object_or_404(Temario, curso=single_curso, slug=temario_slug)
    else:
        single_temario = Temario.objects.filter(curso=single_curso).first()

    for item in list_temarios:
        if item.slug == single_temario.slug:
            item.active = True

    context = {
        'list_cursos': list_cursos,
        'single_curso': single_curso,
        'list_temarios': list_temarios,
        'single_temario': single_temario,
    }
    return render(request, 'cursos_talleres.html', context)

def cortos(request):
    list = OperasPrimasEntries.objects.all()
    list_cortos = Cortometrajes.objects.all()
    context = {
        'list': list,
        'list_cortos': list_cortos,
    }
    return render(request, 'operas_primas_cortometrajes.html', context)

def productora(request):
    context = {}
    return render(request, 'productora_peliculas.html', context)

def plantilla(request):
    context = {}
    return render(request, 'plantilla_docente.html', context)

def otras(request):
    context = {}
    return render(request, 'otras_escuelas.html', context)

def acerca_de(request):
    context = {}
    return render(request, 'operas_primas_cortometrajes.html', context)

def guia_del_alumno(request):
    context = {}
    return render(request, 'operas_primas_cortometrajes.html', context)

def boutique(request):
    context = {}
    return render(request, 'operas_primas_cortometrajes.html', context)

def contacto(request):
    context = {}
    return render(request, 'operas_primas_cortometrajes.html', context)
