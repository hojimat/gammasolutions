from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

def locations(request):
    areas = MarketArea.objects.all()
    cities = City.objects.all()
    return render(request, 'templates/locations.html', {'areas': areas,
                                                        'cities': cities,
                                                        })

def new_city(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created an order.')
            return redirect('/market/locations/')
    else:
        form = CityForm()

    return render(request, "templates/city-form.html", {'form':form})

def read_city(request,pk):
    city = City.objects.get(pk=pk)
    return render(request, "templates/city-details.html", {'city': city})

def delete_city(request,pk):
    city = City.objects.get(pk=pk)
    if request.method == "POST":
        try:
            city.delete()
            messages.warning(request, 'Successfully deleted the driver.')
        except RestrictedError:
            messages.error(request, 'Could not delete the driver. Delete associated orders first.')
            pass

        return redirect('/market/locations/')
        
    return render(request, "templates/delete.html", {'object_name': city})

def edit_city(request,pk):
    city = City.objects.get(pk=pk)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the city information.')
            return redirect('/market/locations/')
    else:
        form = CityForm(instance=city)

    return render(request, "templates/city-form.html", {'form': form})
