from django.shortcuts import redirect, render
from .forms import PositionCTOForm, PositionCEOForm, PositionPoleForm, PositionSteelForm
from .models import *
from equipaments.models import boxs, spliters, poles, steels




def list_ceo(request):
    box = boxs.objects.all()
    ceo = ceos.objects.all()
    pole = positionPoles.objects.all()
    return render(request, 'list-position-ceo.html', {'ceo': ceo, 'box': box, 'pole': pole} )

def position_ceo(request):
    form = PositionCEOForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('inventory:listar-ceos')
   
    return render(request, 'position-ceo.html', {'form': form})

def update_ceo(request, id):
    ceo = ceos.objects.get(id = id)
    form =  PositionCEOForm(request.POST or None, instance=ceo)

    if form.is_valid():
        form.save()
        return redirect('inventory:listar-ceos')
    return render(request, 'position-ceo.html', {'form': form, 'ceo': ceo})

def delete_ceo(request, id):
    ceo = ceos.objects.get(id = id)

    if request.method == 'POST':
        ceo.delete()
        return redirect('inventory:listar-ceos')
    return render(request, 'confirm-delete-ceo.html', {'ceo': ceo})

def list_cto(request):
    box = boxs.objects.all()
    pole = positionPoles.objects.all()
    spliter = spliters.objects.all()
    cto = ctos.objects.all()
    return render(request, 'list-position-cto.html', {'cto': cto, 'box': box, 'spliter': spliter, 'pole': pole})

def position_cto(request):
    form = PositionCTOForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('inventory:listar-ctos')
   
    return render(request, 'position-cto.html', {'form': form})

def update_cto(request, id):
    cto = ctos.objects.get(id = id)
    form =  PositionCTOForm(request.POST or None, instance=cto)

    if form.is_valid():
        form.save()
        return redirect('inventory:listar-ctos')
    return render(request, 'position-cto.html', {'form': form, 'cto': cto})

def delete_cto(request, id):
    cto = ctos.objects.get(id = id)

    if request.method == 'POST':
        cto.delete()
        return redirect('inventory:listar-ctos')
    return render(request, 'confirm-delete-cto.html', {'cto': cto})


def list_pole(request):
    positionPole = positionPoles.objects.all()
    pole = poles.objects.all()
    return render(request, 'list-position-pole.html', {'pole': pole, 'positionPole': positionPole})

def position_pole(request):
    form = PositionPoleForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('inventory:listar-postes')
   
    return render(request, 'position-pole.html', {'form': form})

def update_pole(request, id):
    pole = positionPoles.objects.get(id = id)

    form =  PositionPoleForm(request.POST or None, instance=pole)

    if form.is_valid():
        form.save()
        return redirect('inventory:listar-postes')
    return render(request, 'position-pole.html', {'form': form, 'pole': pole})

def delete_pole(request, id):
    pole = positionPoles.objects.get(id = id)

    if request.method == 'POST':
        pole.delete()
        return redirect('inventory:listar-postes')
    return render(request, 'confirm-delete-position-pole.html', {'pole': pole})

def list_steel(request):
    positionPole = positionPoles.objects.all()
    steel = positionSteels.objects.all()
    modelSteel = steels.objects.all()

    return render(request, 'list-position-steel.html', {'steel': steel, 'positionPole': positionPole, 'modelSteel': modelSteel})

def position_steel(request):
    form = PositionSteelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory:listar-ferragens')
   
    return render(request, 'position-steel.html', {'form': form})

def update_steel(request, id):
    steel = positionSteels.objects.get(id = id)
    form =  PositionSteelForm(request.POST or None, instance=steel)

    if form.is_valid():
        form.save()
        return redirect('inventory:listar-ferragens')
    return render(request, 'position-steel.html', {'form': form, 'steel': steel})

def delete_steel(request, id):
    steel = positionSteels.objects.get(id = id)

    if request.method == 'POST':
        steel.delete()
        return redirect('inventory:listar-ferragens')
    return render(request, 'confirm-delete-position-steel.html', {'steel': steel})




# Create your views here.
