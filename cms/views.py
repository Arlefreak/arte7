from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import *
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template

social = Social.get_solo()
DEFAULT_TITLE = social.title
DEFAULT_DESCRIPTION = social.description
DEFAULT_PREVIEW = social.preview

def home(request):
    form_class = ContactForm

    list_frases = FrasesHome.objects.all()
    list_messages = MessagesHome.objects.all()
    list_mosaicos = MosaicosHome.objects.all()
    list_guia = GuiaAlumnoMessages.objects.all()


    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name',
                ''
            )

            contact_email = request.POST.get(
                'contact_email',
                ''
            )

            contact_phone = request.POST.get(
                'contact_phone',
                ''
            )

            contact_interest = request.POST.get(
                'contact_interest',
                ''
            )

            contact_message = request.POST.get(
                'contact_message',
                ''
            )

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'contact_interest': contact_interest,
                'contact_message': contact_message,
            }
            content = template.render(context)
            if contact_interest == 'CAR':
                send_to = "admisiones@arte7.net"
            else:
                send_to = "info@arte7.net"

            # send_to = "arlefreak@gmail.com"
            send_from = "info@arte7.net"

            email = EmailMessage(
                "Nuevo corre de contacto",
                content,
                send_from,
                [send_to],
                reply_to = [contact_email],
            )

            email.send(fail_silently=False)
            return redirect('home')

    context = {
        'title' : DEFAULT_TITLE,
        'description': DEFAULT_DESCRIPTION,
        'preview': DEFAULT_PREVIEW,
        'form': form_class,
        'list_frases': list_frases,
        'list_messages': list_messages,
        'list_mosaicos': list_mosaicos,
        'list_guia': list_guia,
    }
    return render(request, 'home.html', context)

def carrera(request, slug=None):
    list = PlanDeEstudios.objects.all()
    if slug:
        single = get_object_or_404(PlanDeEstudios, slug = slug)
    else:
        single = PlanDeEstudios.objects.all().first()

    for item in list:
        if item.slug == single.slug:
            item.active = True

    context = {
        'title' : DEFAULT_TITLE,
        'description': DEFAULT_DESCRIPTION,
        'preview': DEFAULT_PREVIEW,
        'list': list,
        'single': single
    }
    return render(request, 'carrera_de_cine.html', context)

def cursos(request, curso_slug=None, temario_slug=None):
    list_cursos = CursosTalleres.objects.all()
    if curso_slug:
        single_curso = get_object_or_404(CursosTalleres, slug = curso_slug)
    else:
        single_curso = CursosTalleres.objects.all().first()

    for item in list_cursos:
        if item.slug == single_curso.slug:
            item.active = True

    list_temarios = Temario.objects.filter(curso=single_curso)
    if temario_slug:
        single_temario = get_object_or_404(Temario, curso=single_curso, slug=temario_slug)
    else:
        single_temario = Temario.objects.filter(curso=single_curso).first()

    for item in list_temarios:
        if item.slug == single_temario.slug:
            item.active = True

    context = {
        'title' : DEFAULT_TITLE,
        'description': DEFAULT_DESCRIPTION,
        'preview': DEFAULT_PREVIEW,
        'list_cursos': list_cursos,
        'single_curso': single_curso,
        'list_temarios': list_temarios,
        'single_temario': single_temario,
    }
    return render(request, 'cursos_talleres.html', context)

def cortos(request):
    list = OperasPrimasEntries.objects.all()
    list_cortos = Cortometrajes.objects.all()
    context = {
        'title' : DEFAULT_TITLE,
        'description': DEFAULT_DESCRIPTION,
        'preview': DEFAULT_PREVIEW,
        'list': list,
        'list_cortos': list_cortos,
    }
    return render(request, 'operas_primas_cortometrajes.html', context)

def productora(request):
    list = Filmografia.objects.all()
    context = {
        'title' : DEFAULT_TITLE,
        'description': DEFAULT_DESCRIPTION,
        'preview': DEFAULT_PREVIEW,
        'list': list,
    }
    return render(request, 'productora_peliculas.html', context)

def plantilla(request):
    list_directiva = Personal.objects.filter(personal_type='DIR')
    list_docente = Personal.objects.filter(personal_type='DOC')
    context = {
        'title' : DEFAULT_TITLE,
        'description': DEFAULT_DESCRIPTION,
        'preview': DEFAULT_PREVIEW,
        'list_directiva': list_directiva,
        'list_docente': list_docente,
    }
    return render(request, 'plantilla_docente.html', context)
