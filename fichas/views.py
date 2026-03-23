from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dueno, Mascota


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


class DuenoUpdateView(UpdateView):
    model = Dueno
    template_name = 'fichas/dueno_form.html'
    fields = ['nombre', 'rut', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('fichas:dueno_lista')


class DuenoDeleteView(DeleteView):
    model = Dueno
    template_name = 'fichas/dueno_confirm_delete.html'
    success_url = reverse_lazy('fichas:dueno_lista')


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


class MascotaUpdateView(UpdateView):
    model = Mascota
    template_name = 'fichas/mascota_form.html'
    fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento', 'dueno']
    success_url = reverse_lazy('fichas:mascota_lista')


class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'fichas/mascota_confirm_delete.html'
    success_url = reverse_lazy('fichas:mascota_lista')