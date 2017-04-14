from django.shortcuts import render, render_to_response

def carrera(request):
   return render_to_response('carrera_de_cine.html')

def cursos(request):
   return render_to_response('cursos_talleres.html')

def productora(request):
   return render_to_response('productora_peliculas.html')

def plantilla(request):
   return render_to_response('plantilla_docente.html')

def otras(request):
   return render_to_response('otras_escuelas.html')

def cortos(request):
   return render_to_response('operas_primas_cortometrajes.html')

