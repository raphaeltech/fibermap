from django.shortcuts import render
from inventory.models import *

def IndexView(request):
	totalPositionCEO = ceos.objects.count()
	totalPositionCTO = ctos.objects.count()
	totalPositionPole = positionPoles.objects.count()

	return render(request, "theme/index.html", {'totalPositionCEO': totalPositionCEO, 
												'totalPositionCTO': totalPositionCTO, 
												'totalPositionPole': totalPositionPole,
												})

	
