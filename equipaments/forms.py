from django import forms
from .models import boxs, cables, steels, poles, spliters


class BoxForm(forms.ModelForm):
    class Meta:
        model = boxs
        fields = ['description', 'model', 'manufacturer']
        

class CableForm(forms.ModelForm):
    class Meta:
        model = cables
        fields = ['description', 'model', 'manufacturer', 'type']

class SteelForm(forms.ModelForm):
    class Meta:
        model = steels
        fields = ['description', 'model', 'manufacturer', 'price']

class PoleForm(forms.ModelForm):
    class Meta:
        model = poles
        fields = ['type']

class SpliterForm(forms.ModelForm):
    class Meta:
        model = spliters
        fields = ['description', 'model', 'manufacturer', 'type']