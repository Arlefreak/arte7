from django.conf.urls import url
from django.contrib import admin
from cms import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.carrera, name='carrera'),
    url(r'^cursos/', views.cursos, name='cursos'),
    url(r'^productora/', views.productora, name='productora'),
    url(r'^plantilla/', views.plantilla, name='plantilla'),
    url(r'^otras/', views.otras, name='otras'),
    url(r'^cortos/', views.cortos, name='cortos'),
]
