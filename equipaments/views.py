from django.shortcuts import redirect, render
from .models import boxs, cables, poles, spliters, steels
from .forms import BoxForm, CableForm, SteelForm, PoleForm, SpliterForm

def list_boxs(request):
    box = boxs.objects.all()
    return render(request, 'list-boxs.html', {'box': box})

def create_box(request):
    form = BoxForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-caixas')
   
    return render(request, 'register-box.html', {'form': form})

def update_box(request, id):
    box = boxs.objects.get(id = id)
    form =  BoxForm(request.POST or None, instance=box)

    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-caixas')
    return render(request, 'register-box.html', {'form': form, 'box': box})

def delete_box(request, id):
    box = boxs.objects.get(id = id)

    if request.method == 'POST':
        box.delete()
        return redirect('equipaments:listar-caixas')
    return render(request, 'confirm-delete-box.html', {'box': box})

def list_cables(request):
    cable = cables.objects.all()
    return render(request, 'list-cable.html', {'cable': cable})

def create_cable(request):
    form = CableForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-cabos')
   
    return render(request, 'register-cable.html', {'form': form})

def update_cable(request, id):
    cable = cables.objects.get(id = id)
    form =  BoxForm(request.POST or None, instance=cable)

    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-cabos')
    return render(request, 'register-cable.html', {'form': form, 'cable': cable})

def delete_cable(request, id):
    cable = cables.objects.get(id = id)

    if request.method == 'POST':
        cable.delete()
        return redirect('equipaments:listar-cabos')
    return render(request, 'confirm-delete-cable.html', {'cable': cable})

def list_poles(request):
    pole = poles.objects.all()
    return render(request, 'list-pole.html', {'pole': pole})

def create_pole(request):
    form = PoleForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-postes')
   
    return render(request, 'register-pole.html', {'form': form})

def update_pole(request, id):
    pole = poles.objects.get(id = id)
    form =  PoleForm(request.POST or None, instance=pole)

    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-postes')
    return render(request, 'register-pole.html', {'form': form, 'pole': pole})

def delete_pole(request, id):
    pole = poles.objects.get(id = id)

    if request.method == 'POST':
        pole.delete()
        return redirect('equipaments:listar-postes')
    return render(request, 'confirm-delete-pole.html', {'pole': pole})

def list_steels(request):
    steel = steels.objects.all()
    return render(request, 'list-steel.html', {'steel': steel})

def create_steel(request):
    form = SteelForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-ferragens')
   
    return render(request, 'register-steel.html', {'form': form})

def update_steel(request, id):
    steel = steels.objects.get(id = id)
    form =  PoleForm(request.POST or None, instance=steel)

    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-ferragens')
    return render(request, 'register-steel.html', {'form': form, 'steel': steel})

def delete_steel(request, id):
    steel = steels.objects.get(id = id)

    if request.method == 'POST':
        steel.delete()
        return redirect('equipaments:listar-ferragens')
    return render(request, 'confirm-delete-steel.html', {'steel': steel})

def list_spliters(request):
    spliter = spliters.objects.all()
    return render(request, 'list-spliter.html', {'spliter': spliter})

def create_spliter(request):
    form = SpliterForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-spliters')
   
    return render(request, 'register-spliter.html', {'form': form})

def update_spliter(request, id):
    spliter = spliters.objects.get(id = id)
    form =  SpliterForm(request.POST or None, instance=spliter)

    if form.is_valid():
        form.save()
        return redirect('equipaments:listar-spliters')
    return render(request, 'register-spliter.html', {'form': form, 'spliter': spliter})

def delete_spliter(request, id):
    spliter = spliters.objects.get(id = id)

    if request.method == 'POST':
        spliter.delete()
        return redirect('equipaments:listar-spliters')
    return render(request, 'confirm-delete-spliter.html', {'spliter': spliter})


