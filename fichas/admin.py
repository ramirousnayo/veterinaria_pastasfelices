from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import Dueno, Mascota, ConsultaMedica


# ── Inlines ───────────────────────────────────────────────────
class MascotaInline(admin.TabularInline):
    model = Mascota
    extra = 1
    fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento']


class ConsultaInline(admin.TabularInline):
    model = ConsultaMedica
    extra = 1
    fields = ['motivo', 'diagnostico', 'tratamiento', 'costo', 'fecha']
    readonly_fields = ['fecha']


# ── DuenoAdmin ────────────────────────────────────────────────
@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'telefono', 'email', 'cantidad_mascotas']
    search_fields = ['nombre', 'rut']
    ordering = ['nombre']
    inlines = [MascotaInline]

    def cantidad_mascotas(self, obj):
        return obj.mascota_set.count()
    cantidad_mascotas.short_description = 'Mascotas'


# ── Filtros Personalizados ────────────────────────────────────
class ConsultaFilter(admin.SimpleListFilter):
    title = 'Consultas'
    parameter_name = 'tiene_consultas'

    def lookups(self, request, model_admin):
        return (
            ('si', 'Con consultas'),
            ('no', 'Sin consultas'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'si':
            return queryset.filter(consultamedica__isnull=False).distinct()
        if self.value() == 'no':
            return queryset.filter(consultamedica__isnull=True)
        return queryset


# ── MascotaAdmin ──────────────────────────────────────────────
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'raza', 'dueno', 'costo_total_consultas']
    search_fields = ['nombre', 'dueno__nombre']
    list_filter = ['especie', ConsultaFilter]
    ordering = ['nombre']
    inlines = [ConsultaInline]

    def costo_total_consultas(self, obj):
        total = obj.consultamedica_set.aggregate(total=Sum('costo'))['total']
        return f"${total:,.0f}" if total else "$0"
    costo_total_consultas.short_description = 'Costo Total'


# ── ConsultaMedicaAdmin ───────────────────────────────────────
@admin.register(ConsultaMedica)
class ConsultaMedicaAdmin(admin.ModelAdmin):
    list_display = ['mascota', 'motivo', 'fecha', 'costo']
    search_fields = ['motivo', 'mascota__nombre']
    list_filter = ['fecha']
    ordering = ['-fecha']
    readonly_fields = ['fecha']
    actions = ['marcar_sin_costo']

    def marcar_sin_costo(self, request, queryset):
        total = queryset.update(costo=0)
        self.message_user(request, f'{total} consulta(s) marcadas como sin costo.')
    marcar_sin_costo.short_description = 'Marcar como sin costo'


# ── UserAdmin personalizado ───────────────────────────────────
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# ── Identidad del panel ───────────────────────────────────────
admin.site.site_header = '🐾 PatasFelices — Panel de Administración'
admin.site.site_title = 'PatasFelices Admin'
admin.site.index_title = 'Gestión de Fichas Veterinarias'