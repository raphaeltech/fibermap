from django import forms
from .models import *

class PositionCEOForm(forms.ModelForm):
    class Meta:
        model = ceos
        fields = ['identification', 'ceoModel', 'pole', 'numberTray', 'numberFusion']

class PositionCTOForm(forms.ModelForm):
    class Meta:
        model = ctos
        fields = ['identification', 'ctoModel', 'pole', 'spliter1', 'spliter2', 'spliter3', 'fusion', 'numberFusion']

class PositionPoleForm(forms.ModelForm):
    class Meta:
        model = positionPoles
        fields = ['identification', 'geolocation', 'poleModel', 'isLocate', 'priceLocation']

class PositionSteelForm(forms.ModelForm):
    class Meta:
        model = positionSteels
        fields = ['identification', 'poleIdentification', 'modelSteel']
