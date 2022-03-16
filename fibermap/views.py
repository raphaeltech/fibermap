from tkinter.messagebox import NO
from django.shortcuts import render
from inventory.models import *
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin


def IndexView(request):
	totalPositionCEO = ceos.objects.count()
	totalPositionCTO = ctos.objects.count()
	totalPositionPole = positionPoles.objects.count()
	
	ceoTotalPrice = ceoprices.objects.all().aggregate(total=Sum('price'))
	ctoTotalPrice = ctoprices.objects.all().aggregate(total=Sum('price'))
	poleTotalPrice = polepriceslocation.objects.all().aggregate(total=Sum('priceLocation'))
	steelTotalPrice = steelprices.objects.all().aggregate(total=Sum('price'))

	if (ceoTotalPrice['total'] == None):
		ceoTotalPrice['total'] = 0

	if (ctoTotalPrice['total'] == None):
		ctoTotalPrice['total'] = 0

	if (poleTotalPrice['total'] == None):
		poleTotalPrice['total'] = 0
	
	if (steelTotalPrice['total'] == None):
		steelTotalPrice['total'] = 20

	valueTotalInventory = (ceoTotalPrice['total'] + ctoTotalPrice['total'] + poleTotalPrice['total'] + steelTotalPrice['total'])
	
	return render(request, "theme/index.html", {'totalPositionCEO': totalPositionCEO, 
												'totalPositionCTO': totalPositionCTO, 
												'totalPositionPole': totalPositionPole,
												'ceoTotalPrice': ceoTotalPrice,
												'ctoTotalPrice': ctoTotalPrice,
												'poleTotalPrice': poleTotalPrice,
												'steelTotalPrice': steelTotalPrice,
												'valueTotalInventory': valueTotalInventory,
												})

	
