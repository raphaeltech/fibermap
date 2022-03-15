from django.shortcuts import redirect, render
from users.forms import UserChangeForm, UserCreationForm

from users.models import *


# Fibermap em uso
def mapHomeView(request):
    return render(request, "theme/mapHome.html", {})


def registerUser(request):
    form = UserCreationForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('users:lista-de-usuarios')
    
    return render(request, 'registerUser.html', {'form': form})


def lisUsers(request):
    user = User.objects.all()
    return render(request, 'listUsers.html', {'user': user})


def updateUser(request, id):
    user = User.objects.get(id = id)
    form =  UserChangeForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('users:lista-de-usuarios')
    return render(request, 'registerUser.html', {'form': form, 'user': user})


# Retorno de views mysql