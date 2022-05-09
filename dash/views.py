from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import RestrictedError
from .models import *
from .forms import OrderForm, DriverForm, BrokerForm
from datetime import datetime, timedelta

def index(request):
    return render(request, 'templates/index.html',)

def main(request):
    return render(request, 'templates/main.html')

# ALL MODELS

def drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'templates/drivers.html', {'drivers': drivers})

def customers(request):
    customers = Broker.objects.all()
    return render(request, 'templates/customers.html', {'customers': customers})

def orders(request):
    orders = Order.objects.all()
    #orders = Order.objects.filter(deliveryDate__gt = ( datetime.today() - timedelta(days=30) ) )
    return render(request, 'templates/orders.html', {'orders': orders})

# READ MODELS

def read_driver(request,pk):
    driver = Driver.objects.get(pk=pk)
    orders = Order.objects.filter(driver=driver)
    return render(request, "templates/details.html", {'user': driver, 'userId': pk, 'orders': orders})

def read_customer(request,pk):
    customer = Broker.objects.get(pk=pk)
    orders = Order.objects.filter(broker=customer)
    return render(request, "templates/details.html", {'user': customer, 'userId': pk, 'orders': orders})

def read_order(request,pk):
    order = Order.objects.get(pk=pk)
    return render(request, "templates/order-details.html", {'order': order})

# CREATE MODELS

def new_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/orders/')
    else:
        form = OrderForm()

    fType = "order"

    return render(request, "templates/new-form.html", {'form':form,'formType':fType})
 
def new_driver(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/drivers/')
    else:
        form = DriverForm()

    fType = "driver"

    return render(request, "templates/new-form.html", {'form':form,'formType':fType})

def new_customer(request):
    if request.method == "POST":
        form = BrokerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/customers/')
    else:
        form = BrokerForm()

    fType = "customer"

    return render(request, "templates/new-form.html", {'form':form,'formType':fType})

# UPDATE MODELS

def edit_driver(request,pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == "POST":
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('/dash/drivers/')
    else:
        form = DriverForm(instance=driver)

    return render(request, "templates/new-form.html", {'form': form})

def edit_customer(request,pk):
    customer = Broker.objects.get(pk=pk)
    if request.method == "POST":
        form = BrokerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/dash/customers/')
    else:
        form = BrokerForm(instance=customer)

    return render(request, "templates/new-form.html", {'form': form})

def edit_order(request,pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/dash/orders/')
    else:
        form = OrderForm(instance=order)

    return render(request, "templates/new-form.html", {'form': form})

# DELETE MODELS

def delete_driver(request,pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == "POST":
        try:
            driver.delete()
        except RestrictedError:
            pass

        return redirect('/dash/drivers/')
        
    return render(request, "templates/delete.html", {'object_name': driver})

def delete_customer(request,pk):
    customer = Broker.objects.get(pk=pk)
    if request.method == "POST":
        try:
            customer.delete()
        except RestrictedError:
            pass

        return redirect('/dash/customers/')
        
    return render(request, "templates/delete.html", {'object_name': customer})

def delete_order(request,pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        try:
            order.delete()
        except RestrictedError:
            pass

        return redirect('/dash/orders/')
        
    return render(request, "templates/delete.html", {'object_name': f"Order #{pk}"})
