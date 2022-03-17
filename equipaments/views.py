from django.urls import reverse, reverse_lazy
from .models import boxs, cables, poles, spliters, steels
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

### Views para Boxs ###
class createBox(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = boxs
    fields = ['description', 'model', 'manufacturer', 'price']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarcaixas')

class updateBox(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = boxs
    fields = ['description', 'model', 'manufacturer', 'price']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarcaixas')

class deleteBox(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = boxs
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('equipaments:listarcaixas')

class listBox(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = boxs
    template_name = 'boxlist.html'

### Views para Cables ###
class createCable(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = cables
    fields = ['description', 'model', 'manufacturer', 'priceForMetter', 'type']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarcabos')

class updateCable(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = cables
    fields = ['description', 'model', 'manufacturer', 'priceForMetter', 'type']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarcabos')

class deleteCable(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = cables
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('equipaments:listarcabos')

class listCable(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = cables
    template_name = 'cablelist.html'

### Views para Ferragens ###
class createSteel(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = steels
    fields = ['description', 'model', 'manufacturer', 'price']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarferragens')

class updateSteel(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = steels
    fields = ['description', 'model', 'manufacturer', 'price']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarferragens')

class deleteSteel(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = steels
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('equipaments:listarferragens')

class listSteel(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = steels
    template_name = 'steellist.html'

### Views para Postes ###
class createPole(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = poles
    fields = ['type']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarpostes')

class updatePole(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = poles
    fields = ['type']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarpostes')

class deletePole(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = poles
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('equipaments:listarpostes')

class listPole(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = poles
    template_name = 'polelist.html'

### Views para Spliter ###
class createSpliter(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = spliters
    fields = ['description', 'model', 'manufacturer', 'type', 'price']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarspliters')

class updateSplite(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = spliters
    fields = ['description', 'model', 'manufacturer', 'type', 'price']
    template_name = 'form.html'
    success_url = reverse_lazy('equipaments:listarspliters')

class deleteSpliter(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = spliters
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('equipaments:listarspliters')

class listSpliter(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = spliters
    template_name = 'spliterlist.html'


