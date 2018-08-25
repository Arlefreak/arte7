__author__ = 'Arlefreak'
# -*- coding: utf-8 -*-
from django.urls import reverse


def menu(request):
    menu = {"menu": [
        {'name': 'carrera de cine', 'url': reverse('carrera')},
        {'name': 'cursos / talleres', 'url': reverse('cursos')},
        {'name': 'Óperas primas / cortometrajes', 'url': reverse('cortos')},
        {'name': 'productora / PELÍCULAS', 'url': reverse('productora')},
        {'name': 'plantilla docente', 'url': reverse('plantilla')},
        {'name': 'otras escuelas', 'url': reverse('home') + '#otras-escuelas'},
        {'name': 'boutique', 'url': reverse('home') + "#boutique"},
        {'name': 'revista', 'url': 'https://www.arte7qro.net/blog/' },
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu

def footer_menu(request):
    footer_menu = {"footer_menu": [
        {'name': 'acerca de', 'url': reverse('home') + "#acerca"},
        {'name': 'guia del alumno', 'url': reverse('home') + "#guia"},
        {'name': 'contacto', 'url': reverse('home') + "#contacto"},
    ]}
    for item in footer_menu['footer_menu']:
        if request.path == item['url']:
            item['active'] = true
    return footer_menu
