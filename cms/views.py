from django.shortcuts import render, render_to_response

def carrera(request):
    context = {}
    return render(request, 'carrera_de_cine.html', context)

def cursos(request):
    context = {}
    return render(request, 'cursos_talleres.html', context)

def productora(request):
    context = {}
    return render(request, 'productora_peliculas.html', context)

def plantilla(request):
    context = {}
    return render(request, 'plantilla_docente.html', context)

def otras(request):
    context = {}
    return render(request, 'otras_escuelas.html', context)

def cortos(request):
    context = {}
    return render(request, 'operas_primas_cortometrajes.html', context)


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
