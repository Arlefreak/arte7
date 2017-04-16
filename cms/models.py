from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

def upload_to(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'uploads/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

class CarreraDeCine(SingletonModel):
    description = RichTextField()
    message_title = models.CharField(max_length=140)
    message_body = RichTextField()
    second_description = RichTextField()
    def __str__(self):
        return "Carrera de cine"

class PlanDeEstudios(models.Model):
    title = models.CharField(max_length=140)
    description = RichTextField()

class CursosTalleres(models.Model):
    description = RichTextField()
    message_title = models.CharField(max_length=140)
    message_body = RichTextField()
    second_description = RichTextField()

class Temario(models.Model):
    curso = models.ForeignKey('CursosTalleres')
    title = models.CharField(max_length=140)
    description = RichTextField()

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

class Productora(SingletonModel):
    description = RichTextField()
    second_description = RichTextField()

class Filmografia(models.Model):
    title = models.CharField(max_length=140)
    description = RichTextField()
    video = EmbedVideoField()

class Publicidad(SingletonModel):
    description = RichTextField()
    video = EmbedVideoField()

class Personal(models.Model):
    name = models.CharField(max_length=140)
    avatart = models.ImageField(upload_to=upload_to)
    role = models.CharField(max_length=140)
    description = RichTextField()
    url = models.URLField()

