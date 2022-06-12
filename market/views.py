from django.shortcuts import render
from .models import *

def areas(request):
    areas = MarketArea.objects.all()
    return render(request, 'templates/areas.html', {'areas': areas})
