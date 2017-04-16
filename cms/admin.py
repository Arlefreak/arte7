from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import CarreraDeCine, PlanDeEstudios

@admin.register(CarreraDeCine)
class CarreraDeCineAdmin(SingletonModelAdmin):
    fields = (
        'description',
        'message_title',
        'message_body',
        'second_description',
    )

@admin.register(PlanDeEstudios)
class PlanDeEstudiosAdmin(admin.ModelAdmin):
    fields = ('title',)
