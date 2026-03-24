from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Dueno, Mascota, ConsultaMedica



# ── Vistas de Dueño ──────────────────────────────────────────
class DuenoListView(ListView):
    model = Dueno
    template_name = 'fichas/dueno_list.html'
    context_object_name = 'duenos'


class DuenoDetailView(DetailView):
    model = Dueno
    template_name = 'fichas/dueno_detail.html'
    context_object_name = 'dueno'


class DuenoCreateView(CreateView):
    model = Dueno
    template_name = 'fichas/dueno_form.html'
    fields = ['nombre', 'rut', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('fichas:dueno_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Dueño creado correctamente.')
        return super().form_valid(form)


class DuenoUpdateView(UpdateView):
    model = Dueno
    template_name = 'fichas/dueno_form.html'
    fields = ['nombre', 'rut', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('fichas:dueno_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Dueño actualizado correctamente.')
        return super().form_valid(form)


class DuenoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dueno
    template_name = 'fichas/dueno_confirm_delete.html'
    success_url = reverse_lazy('fichas:dueno_lista')
    permission_required = 'fichas.delete_dueno'

    def form_valid(self, form):
        messages.success(self.request, 'Dueño eliminado correctamente.')
        return super().form_valid(form)

# ── Vistas de Mascota ─────────────────────────────────────────
class MascotaListView(ListView):
    model = Mascota
    template_name = 'fichas/mascota_list.html'
    context_object_name = 'mascotas'


class MascotaDetailView(DetailView):
    model = Mascota
    template_name = 'fichas/mascota_detail.html'
    context_object_name = 'mascota'


class MascotaCreateView(CreateView):
    model = Mascota
    template_name = 'fichas/mascota_form.html'
    fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento', 'dueno']
    success_url = reverse_lazy('fichas:mascota_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Mascota creada correctamente.')
        return super().form_valid(form)


class MascotaUpdateView(UpdateView):
    model = Mascota
    template_name = 'fichas/mascota_form.html'
    fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento', 'dueno']
    success_url = reverse_lazy('fichas:mascota_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Mascota actualizada correctamente.')
        return super().form_valid(form)


class MascotaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'fichas/mascota_confirm_delete.html'
    success_url = reverse_lazy('fichas:mascota_lista')
    permission_required = 'fichas.delete_mascota'

    def form_valid(self, form):
        messages.success(self.request, 'Mascota eliminada correctamente.')
        return super().form_valid(form)


# ── Vistas de Consulta Médica ─────────────────────────────────
class ConsultaListView(ListView):
    model = ConsultaMedica
    template_name = 'fichas/consulta_list.html'
    context_object_name = 'consultas'


class ConsultaDetailView(DetailView):
    model = ConsultaMedica
    template_name = 'fichas/consulta_detail.html'
    context_object_name = 'consulta'


class ConsultaCreateView(CreateView):
    model = ConsultaMedica
    template_name = 'fichas/consulta_form.html'
    fields = ['mascota', 'motivo', 'diagnostico', 'tratamiento', 'costo']
    success_url = reverse_lazy('fichas:consulta_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Consulta creada correctamente.')
        return super().form_valid(form)


class ConsultaUpdateView(UpdateView):
    model = ConsultaMedica
    template_name = 'fichas/consulta_form.html'
    fields = ['mascota', 'motivo', 'diagnostico', 'tratamiento', 'costo']
    success_url = reverse_lazy('fichas:consulta_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Consulta actualizada correctamente.')
        return super().form_valid(form)


class ConsultaDeleteView(DeleteView):
    model = ConsultaMedica
    template_name = 'fichas/consulta_confirm_delete.html'
    success_url = reverse_lazy('fichas:consulta_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Consulta eliminada correctamente.')
        return super().form_valid(form)


# ── Vista de Inicio ───────────────────────────────────────────
def inicio(request):
    context = {
        'total_duenos': Dueno.objects.count(),
        'total_mascotas': Mascota.objects.count(),
        'total_consultas': ConsultaMedica.objects.count(),
    }
    return render(request, 'fichas/inicio.html', context)