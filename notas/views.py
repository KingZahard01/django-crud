# Create your views here.
from audioop import reverse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from notas.models import Nota

# vistas basadas en clases

# GET
# Muestra notas
class HomePageView(ListView):
    # template_name = 'notas/home.html'
    model = Nota

# POST
# Crea notas
class CreateNotaView(CreateView):
    # template_name = 'notas/nuevo.html'
    model = Nota
    fields = ['titulo', 'descripcion']
    # forma 1 de usar reverse_lazy
    def get_success_url(self):
        return reverse_lazy('home')

# PUT / PATCH
# Actualizar notas
class UpdateNotaView(UpdateView):
    template_name = 'notas/nota_update_form.html'
    model = Nota
    fields = ['titulo', 'descripcion']
    # forma 2 de usar reverse_lazy
    success_url = reverse_lazy('home')

# DELETE
# Eliminar notas
class DeleteNotaView(DeleteView):
    # template_name = 'notas/eliminar.html'
    model = Nota
    success_url = reverse_lazy('home')