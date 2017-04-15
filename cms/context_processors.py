__author__ = 'Arlefreak'
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse


def menu(request):
    menu = {"menu": [
        {'name': 'carrera de cine', 'url': reverse('carrera')},
        {'name': 'cursos / talleres', 'url': reverse('cursos')},
        {'name': 'productora / peliculas', 'url': reverse('productora')},
        {'name': 'plantilla docente', 'url': reverse('plantilla')},
        {'name': 'otras escuelas', 'url': reverse('otras')},
        {'name': 'operas primas', 'url': reverse('cortos')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu

def footer_menu(request):
    footer_menu = {"footer_menu": [
        {'name': 'acerca de', 'url': reverse('acerca_de')},
        {'name': 'guia del alumno', 'url': reverse('guia_del_alumno')},
        {'name': 'boutique', 'url': reverse('boutique')},
        {'name': 'contacto', 'url': reverse('contacto')},
    ]}
    for item in footer_menu['footer_menu']:
        if request.path == item['url']:
            item['active'] = True
    return footer_menu
