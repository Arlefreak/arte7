from adminsortable.admin import SortableAdmin
from django.contrib import admin
from django.utils.safestring import mark_safe
from embed_video.admin import AdminVideoMixin
from embed_video.backends import VideoBackend
from solo.admin import SingletonModelAdmin

from .models import (
    Boutique, CarreraDeCine, Contacto, Cortometrajes, CursosTalleres,
    Filmografia, FrasesHome, GuiaAlumnoMessages, Home, MessagesHome,
    MosaicosHome, OperasPrimas, OperasPrimasEntries, Partners, Personal,
    PlanDeEstudios, Productora, Publicidad, Social, Temario, Video)


class ViewOnSiteMixin(object):
    @mark_safe
    def view_on_site(self, obj):
        url = obj.get_absolute_url()
        return f"<a class='button' href='{url}'>view on site</a>"

    view_on_site.allow_tags = True
    view_on_site.short_description = u"View on site"


class AdminImageMixin(object):
    @mark_safe
    def admin_image(self, obj):
        return f"""<img
                        src='{obj.image.url}'
                        style='height: 100px; width: auto; display: block'
                    />
                """

    admin_image.allow_tags = True
    admin_image.short_description = u"Preview"


# class AdminVideoMixin2(object):
#     def admin_video_thumbnail(self, obj):
#         return u"<img src='%s' />" % VideoBackend(obj.video).thumbnail
#     admin_video_thumbnail.allow_tags = True
#     admin_video_thumbnail.short_description = u"Video"

# @admin.register(CKTest)
# class CKtest(SingletonModelAdmin):
#     pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin, AdminImageMixin):
    list_display = ('admin_image', 'get_embed_link')
    list_display_links = ('admin_image', )


@admin.register(Social)
class SocialAdmin(SingletonModelAdmin):
    pass


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


@admin.register(OperasPrimas)
class OperasPrimasAdmin(AdminVideoMixin, SingletonModelAdmin):
    pass


@admin.register(OperasPrimasEntries)
class OperasPrimasEntriesAdmin(ViewOnSiteMixin, AdminVideoMixin, SortableAdmin,
                               AdminImageMixin):
    save_as = True
    list_display = (
        'order',
        'title',
        'view_on_site',
        'admin_image',
    )
    list_display_links = (
        'order',
        'title',
        'admin_image',
    )


@admin.register(Cortometrajes)
class CortometrajesAdmin(AdminImageMixin, ViewOnSiteMixin, AdminVideoMixin,
                         SortableAdmin):
    save_as = True
    list_display = (
        'order',
        'title',
        'admin_image',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'admin_image',
        'title',
    )


@admin.register(Productora)
class ProductoraAdmin(AdminVideoMixin, SingletonModelAdmin):
    pass


@admin.register(Publicidad)
class PublicidadAdmin(AdminVideoMixin, SingletonModelAdmin):
    pass


@admin.register(Filmografia)
class FilmografiaAdmin(AdminImageMixin, ViewOnSiteMixin, SortableAdmin):
    save_as = True
    list_display = (
        'order',
        'title',
        'admin_image',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'title',
        'admin_image',
    )


@admin.register(Personal)
class PersonalAdmin(AdminImageMixin, ViewOnSiteMixin, SortableAdmin):
    save_as = True
    list_display = (
        'order',
        'name',
        'personal_type',
        'role',
        'admin_image',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'name',
        'role',
        'admin_image',
    )
    list_editable = ('personal_type', )
    list_filter = ('personal_type', )


@admin.register(FrasesHome)
class FrasesHomeAdmin(ViewOnSiteMixin, SortableAdmin):
    save_as = True
    list_display = (
        'order',
        'title',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'title',
    )


@admin.register(MessagesHome)
class MessagesHomeAdmin(ViewOnSiteMixin, SortableAdmin):
    save_as = True
    list_display = (
        'order',
        'title',
        'link',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'title',
        'link',
    )
    # list_editable = (
    #     'link',
    # )


@admin.register(MosaicosHome)
class MosaicosHomeAdmin(AdminImageMixin, ViewOnSiteMixin, SortableAdmin):
    save_as = True
    list_display = (
        'order',
        'title',
        'link',
        'admin_image',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'title',
        'admin_image',
        'link',
    )


@admin.register(Home)
class HomeAdmin(AdminVideoMixin, SingletonModelAdmin):
    pass


@admin.register(Boutique)
class BoutiqueAdmin(SingletonModelAdmin):
    pass


@admin.register(Contacto)
class ContactoAdmin(SingletonModelAdmin):
    pass


@admin.register(GuiaAlumnoMessages)
class GuiaAlumnoMessagesAdmin(ViewOnSiteMixin, SortableAdmin):
    save_as = True
    list_display = (
        'order',
        'title',
        'file',
        'view_on_site',
    )
    list_display_links = (
        'order',
        'title',
        'file',
    )


@admin.register(Partners)
class PartnersAdmin(SortableAdmin, AdminImageMixin):
    list_display = ('name', 'admin_image', 'link')
    list_display_links = (
        'name',
        'admin_image',
    )
