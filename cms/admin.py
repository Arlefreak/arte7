from django.contrib import admin
from solo.admin import SingletonModelAdmin
from adminsortable.admin import SortableAdmin
from .models import *

class ViewOnSiteMixin(object):
    def view_on_site(self, obj):
        return u"<a class='button' href='%s'>view on site</a>" % obj.get_absolute_url()
    view_on_site.allow_tags = True
    view_on_site.short_description = u"View on site"

@admin.register(CarreraDeCine)
class CarreraDeCineAdmin(SingletonModelAdmin):
    pass

@admin.register(PlanDeEstudios)
class PlanDeEstudiosAdmin(ViewOnSiteMixin, SortableAdmin):
    list_display = (
        'order',
        'title',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'title',
    )

@admin.register(CursosTalleres)
class CursosTalleresAdmin(ViewOnSiteMixin, SortableAdmin):
    list_display = (
        'order',
        'title',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'title',
    )

@admin.register(Temario)
class TemarioAdmin(ViewOnSiteMixin, SortableAdmin):
    list_display = (
        'order',
        'curso',
        'title',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'title',
        'curso',
    )
    list_filter = ('curso', )
