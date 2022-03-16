from django.shortcuts import redirect, render
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# controle de usuario
from django.contrib.auth.mixins import LoginRequiredMixin

### Views para CEO ###
class createPositionCeo(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = ceos
    fields = ['identification', 'ceoModel', 'pole', 'numberTray', 'numberFusion']
    template_name = 'form.html'
    success_url = reverse_lazy('listarceos')

class updatePositionCeo(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = ceos
    fields = ['identification', 'ceoModel', 'pole', 'numberTray', 'numberFusion']
    template_name = 'form.html'
    success_url = reverse_lazy('listarceos')

class deletePositionCeo(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = ceos
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listarceos')

class listPositionCeo(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = ceos
    template_name = 'ceolist.html'

### Views para CTO ###
class createPositionCto(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = ctos
    fields = ['identification', 'ctoModel', 'pole', 'spliter1', 'spliter2', 'spliter3', 'fusion', 'numberFusion']
    template_name = 'form.html'
    success_url = reverse_lazy('listarctos')

class updatePositionCto(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = ctos
    fields = ['identification', 'ctoModel', 'pole', 'spliter1', 'spliter2', 'spliter3', 'fusion', 'numberFusion']
    template_name = 'form.html'
    success_url = reverse_lazy('listarctos')

class deletePositionCto(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = ctos
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listarctos')

class listPositionCto(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = ctos
    template_name = 'ctolist.html'

### Views para Postes ###
class createPositionPole(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = positionPoles
    fields = ['identification', 'geolocation', 'poleModel', 'isLocate', 'priceLocation']
    template_name = 'form.html'
    success_url = reverse_lazy('listarpostes')

class updatePositionPole(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = positionPoles
    fields = ['identification', 'geolocation', 'poleModel', 'isLocate', 'priceLocation']
    template_name = 'form.html'
    success_url = reverse_lazy('listarpostes')

class deletePositionPole(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = positionPoles
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listarpostes')

class listPositionPole(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = positionPoles
    template_name = 'polelist.html'

### Views para Ferragens ###
class createPositionSteel(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = positionSteels
    fields = ['identification', 'modelSteel', 'poleIdentification']
    template_name = 'form.html'
    success_url = reverse_lazy('listarferragens')

class updatePositionSteel(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = positionSteels
    fields = ['identification', 'modelSteel', 'poleIdentification']
    template_name = 'form.html'
    success_url = reverse_lazy('listarferragens')

class deletePositionSteel(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = positionSteels
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listarferragens')

class listPositionSteel(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = positionSteels
    template_name = 'steellist.html'
