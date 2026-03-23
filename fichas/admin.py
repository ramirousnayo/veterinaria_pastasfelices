from django.contrib import admin
from .models import Dueno, Mascota, ConsultaMedica


@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'telefono', 'email']
    search_fields = ['nombre', 'rut']


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'raza', 'dueno']
    search_fields = ['nombre', 'especie']


@admin.register(ConsultaMedica)
class ConsultaMedicaAdmin(admin.ModelAdmin):
    list_display = ['mascota', 'motivo', 'fecha', 'costo']
    search_fields = ['motivo', 'mascota__nombre']