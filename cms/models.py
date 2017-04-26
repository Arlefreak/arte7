from django.db import models
from django.template import defaultfilters
from solo.models import SingletonModel
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
import os

PERSONAL_CHOICES = (
    ('DIR', 'Directiva'),
    ('DOC', 'Plantilla Docente'),
)

PAGES = (
    ('CAR', 'carrera de cine'),
    ('CUR', 'cursos / talleres'),
    ('OPE', 'Óperas primas / cortometrajes'),
    ('PRO', 'productora / películas'),
    ('PLA', 'plantilla docente'),
    ('HOM', 'home'),
)

def upload_to(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'uploads/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

class CKTest(SingletonModel):
    file = RichTextUploadingField()

class CarreraDeCine(SingletonModel):
    video = EmbedVideoField()
    description = RichTextUploadingField()
    message_title = models.CharField(max_length=140)
    message_body = RichTextUploadingField()
    second_description = RichTextUploadingField()
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

class OperasPrimas(SingletonModel):
    video = EmbedVideoField()
    description = RichTextField()
    def __str__(self):
        return 'Operas Primas'

class OperasPrimasEntries(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    video = EmbedVideoField()
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    description = RichTextField()
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(OperasPrimasEntries, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('cortos')
    class Meta:
        verbose_name = 'Opera Prima Video'
        verbose_name_plural = 'Operas Primas Videos'
        ordering = ['order']
    def __str__(self):
        return self.title

class Cortometrajes(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    video = EmbedVideoField()
    image = models.ImageField(upload_to=upload_to)
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    description = RichTextField()
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(Cortometrajes, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('cortos')
    class Meta:
        verbose_name = 'Cortometraje'
        verbose_name_plural = 'Cortometrajes'
        ordering = ['order']
    def __str__(self):
        return self.title

class Productora(SingletonModel):
    video = EmbedVideoField()
    description = RichTextField()

class Publicidad(SingletonModel):
    video = EmbedVideoField()
    description = RichTextField()

class Filmografia(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    image = models.ImageField(upload_to=upload_to)
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    description = RichTextField()
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(Filmografia, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('productora')
    class Meta:
        verbose_name = 'Entrada de filmografia'
        verbose_name_plural = 'Entradas de filmografia'
        ordering = ['order']
    def __str__(self):
        return self.title

class Personal(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    image = models.ImageField(upload_to=upload_to)
    name = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    personal_type = models.CharField(max_length=3, choices=PERSONAL_CHOICES, default='DOC')
    role = models.CharField(max_length=140)
    description = RichTextField()
    url = models.URLField(blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Personal, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('plantilla')
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'
        ordering = ['order']
    def __str__(self):
        return self.name

class Home(SingletonModel):
    video = EmbedVideoField()
    description = RichTextField()
    description_objetivo = RichTextField()
    image_objetivo = models.ImageField(upload_to=upload_to)
    description_resolucion = RichTextField()
    image_resolucion = models.ImageField(upload_to=upload_to)
    link_frente = models.URLField(blank=True, null=True)
    image_frente = models.FileField(upload_to=upload_to)
    link_plataforma = models.URLField(blank=True, null=True)
    image_plataforma = models.FileField(upload_to=upload_to)

class GuiaAlumnoMessages(SortableMixin):
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    file = models.FileField(upload_to=upload_to)
    description = RichTextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(GuiaAlumnoMessages, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('home')
    class Meta:
        verbose_name = 'Mensaje guia del alumno'
        verbose_name_plural = 'Mensajes guia del alumno'
        ordering = ['order']
    def __str__(self):
        return self.title 

class Boutique(SingletonModel):
    description = RichTextField()
    link = models.URLField()

class Contacto(SingletonModel):
    title = models.CharField(max_length=140)
    description = RichTextField()

class FrasesHome(SortableMixin):
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(FrasesHome, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('home')
    class Meta:
        verbose_name = 'Frase del home'
        verbose_name_plural = 'Frases del home'
        ordering = ['order']
    def __str__(self):
        return self.title 

class MessagesHome(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    link = models.URLField()
    title = models.CharField(max_length=140)
    slug  = models.CharField(max_length=200, editable=False)
    description = RichTextField()
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(MessagesHome, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('home')
    class Meta:
        verbose_name = 'Mensaje del home'
        verbose_name_plural = 'Mensajes del home'
        ordering = ['order']
    def __str__(self):
        return self.title 

class MosaicosHome(SortableMixin):
    title = models.CharField(max_length=140)
    link = models.URLField()
    slug  = models.CharField(max_length=200, editable=False)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    image = models.ImageField(upload_to=upload_to)
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(MosaicosHome, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('home')
    class Meta:
        verbose_name = 'Mosaico del home'
        verbose_name_plural = 'Mosaicos del home'
        ordering = ['order']
    def __str__(self):
        return self.title 

class Social(SingletonModel):
    facebook = models.URLField()
    instagram = models.URLField()
    vimeo = models.URLField()

