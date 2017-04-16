from django.db import models
from django.template import defaultfilters
from solo.models import SingletonModel
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse

def upload_to(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'uploads/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

class CarreraDeCine(SingletonModel):
    video = EmbedVideoField()
    description = RichTextField()
    message_title = models.CharField(max_length=140)
    message_body = RichTextField()
    second_description = RichTextField()
    def __str__(self):
        return "Carrera de cine"

class PlanDeEstudios(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    description = RichTextField()
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(PlanDeEstudios, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('carrera', args=[self.slug])
    class Meta:
        verbose_name = 'Plan de estudios'
        verbose_name_plural = 'Planes de estudio'
        ordering = ['order']
    def __str__(self):
        return self.title

class CursosTalleres(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    video = EmbedVideoField()
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    description = RichTextField()
    message_title = models.CharField(max_length=140)
    message_body = RichTextField()
    second_description = RichTextField()
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(CursosTalleres, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('cursos', args=[self.slug])
    class Meta:
        verbose_name = 'CursoTaller'
        verbose_name_plural = 'CursosTalleres'
        ordering = ['order']
    def __str__(self):
        return self.title

class Temario(SortableMixin):
    curso = SortableForeignKey('CursosTalleres')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    description = RichTextField()
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(Temario, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('cursos', args=[self.curso.slug, self.slug])
    class Meta:
        verbose_name = 'Temario'
        verbose_name_plural = 'Temarios'
        ordering = ['order']
    def __str__(self):
        return self.title

class Productora(SingletonModel):
    video = EmbedVideoField()
    description = RichTextField()

class Publicidad(SingletonModel):
    video = EmbedVideoField()
    description = RichTextField()

class Filmografia(models.Model):
    title = models.CharField(max_length=140)
    description = RichTextField()
    video = EmbedVideoField()

class OperasPrimas(SingletonModel):
    description = RichTextField()
    second_description = RichTextField()

class OperasPrimasEntries(models.Model):
    title = models.CharField(max_length=140)
    description = RichTextField()
    video = EmbedVideoField()

class Cortometrajes(models.Model):
    title = models.CharField(max_length=140)
    description = RichTextField()
    video = EmbedVideoField()

class Personal(models.Model):
    name = models.CharField(max_length=140)
    avatart = models.ImageField(upload_to=upload_to)
    role = models.CharField(max_length=140)
    description = RichTextField()
    url = models.URLField()

