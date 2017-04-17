__author__ = 'Arlefreak'
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse


def menu(request):
    menu = {"menu": [
        {'name': 'carrera de cine', 'url': reverse('carrera')},
        {'name': 'cursos / talleres', 'url': reverse('cursos')},
        {'name': 'Óperas primas / cortometrajes', 'url': reverse('cortos')},
        {'name': 'productora / PELÍCULAS', 'url': reverse('productora')},
        {'name': 'plantilla docente', 'url': reverse('plantilla')},
        {'name': 'otras escuelas', 'url': reverse('home')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu

def footer_menu(request):
    footer_menu = {"footer_menu": [
        {'name': 'acerca de', 'url': reverse('home')},
        {'name': 'guia del alumno', 'url': reverse('home')},
        {'name': 'boutique', 'url': reverse('home')},
        {'name': 'contacto', 'url': reverse('home')},
    ]}
    for item in footer_menu['footer_menu']:
        if request.path == item['url']:
            item['active'] = False
    return footer_menu
