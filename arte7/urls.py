from django.conf.urls import url, include
from django.contrib import admin
from cms import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^gracias/$', views.home, name='gracias'),
    # url(r'^test/$', views.test, name='test'),

    url(r'^carrera/$', views.carrera, name='carrera'),
    url(r'^carrera/(?P<slug>[\w-]+)/$', views.carrera , name='carrera'),

    url(r'^cursos/$', views.cursos, name='cursos'),
    url(r'^cursos/(?P<curso_slug>[\w-]+)/$', views.cursos , name='cursos'),
    url(r'^cursos/(?P<curso_slug>[\w-]+)/(?P<temario_slug>[\w-]+)/$', views.cursos , name='cursos'),

    url(r'^productora/$', views.productora, name='productora'),
    url(r'^plantilla/$', views.plantilla, name='plantilla'),
    url(r'^cortos/$', views.cortos, name='cortos'),
]
