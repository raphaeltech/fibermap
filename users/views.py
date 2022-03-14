from django.shortcuts import redirect, render
from users.forms import UserChangeForm, UserCreationForm

from users.models import *

def LoginView(request):
    return render(request, "theme/login.html", {})

def RegisterView(request):
    return render(request, "theme/register.html", {})

def ForgotPasswordView(request):
    return render(request, "theme/forgot-password.html", {})

def LogoutView(request):
    return render(request, "theme/forgot-password.html", {})

def ChartsView(request):
    return render(request, "theme/charts.html", {})

def TablesView(request):
    return render(request, "theme/tables.html", {})

def LogoutView(request):
    return render(request, "theme/forgot-password.html", {})

def ButtonsView(request):
    return render(request, "theme/buttons.html", {})

def CardsView(request):
    return render(request, "theme/cards.html", {})

def PageNotFoundView(request):
    return render(request, "theme/404.html", {})

def BlankView(request):
    return render(request, "theme/blank.html", {})

def ColorsView(request):
    return render(request, "theme/utilities-color.html", {})

def BordersView(request):
    return render(request, "theme/utilities-border.html", {})

def AnimationsView(request):
    return render(request, "theme/utilities-animation.html", {})

def OthersView(request):
    return render(request, "theme/utilities-other.html", {})

def DashboardView(request):
        return render(request, "users/dashboard.html", {})


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

"""    

def registerTypeUser(request):
    form = typeUserModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user:cadastrar-tipos-de-usuarios')
    
    return render(request, 'registerTypeUser.html', {'form': form})

def registerCompany(request):
    form = companyModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user:cadastrar-empresa')
    
    return render(request, 'registerCompany.html', {'form': form})
"""
