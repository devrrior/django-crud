from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from notas.models import Nota
from notas.forms import NotaForm

# GET
# Muestre mis notas
class HomePageView(ListView):
  # template_name = 'notas/home.html'
  model = Nota

# POST
# Cree notas
class CreateNotaView(CreateView):
  # template_name = 'notas/nuevo.html'
  model = Nota
  form_class= NotaForm
  # fields = ['titulo', 'descripcion']
  success_url = reverse_lazy('home')


# PUT / PATCH
# Actualizar notas
class UpdateNotaView(UpdateView):
  # template_name = 'notas/actualizar.html'
  model = Nota
  form_class= NotaForm
  # fields = ['titulo', 'descripcion']
  success_url = reverse_lazy('home')

# DELETE
# Eliminar Notas
class DeleteNotaView(DeleteView):
  # template_name = 'notas/eliminar.html'
  model = Nota
  success_url = reverse_lazy('home')
