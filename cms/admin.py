from django.contrib import admin
from solo.admin import SingletonModelAdmin
from adminsortable.admin import SortableAdmin
from embed_video.admin import AdminVideoMixin
from embed_video.backends import VideoBackend
from .models import *

class ViewOnSiteMixin(object):
    def view_on_site(self, obj):
        return u"<a class='button' href='%s'>view on site</a>" % obj.get_absolute_url()
    view_on_site.allow_tags = True
    view_on_site.short_description = u"View on site"

# class AdminVideoMixin2(object):
#     def admin_video_thumbnail(self, obj):
#         return u"<img src='%s' />" % VideoBackend(obj.video).thumbnail
#     admin_video_thumbnail.allow_tags = True
#     admin_video_thumbnail.short_description = u"Video"

@admin.register(CarreraDeCine)
class CarreraDeCineAdmin(AdminVideoMixin, SingletonModelAdmin):
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
class CursosTalleresAdmin(AdminVideoMixin, ViewOnSiteMixin, SortableAdmin):
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

@admin.register(Productora)
class ProductoraAdmin(AdminVideoMixin, SingletonModelAdmin):
    pass

@admin.register(Publicidad)
class PublicidadAdmin(AdminVideoMixin, SingletonModelAdmin):
    pass
