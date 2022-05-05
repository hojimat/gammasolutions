from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import OrderForm, DriverForm, CustomerForm
from datetime import datetime, timedelta

def index(request):
    return render(request, 'templates/index.html',)

def main(request):
    return render(request, 'templates/main.html')

def drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'templates/drivers.html', {'drivers': drivers})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'templates/customers.html', {'customers': customers})

def orders(request):
    orders = Order.objects.all()
    #orders = Order.objects.filter(deliveryDate__gt = ( datetime.today() - timedelta(days=30) ) )
    return render(request, 'templates/orders.html', {'orders': orders})

def readDriver(request,pk):
    driver = Driver.objects.get(pk=pk)
    orders = Order.objects.filter(driver=driver)
    return render(request, "templates/details.html", {'userId': pk, 'orders': orders, 'userName': f"{driver.firstName} {driver.lastName}"})

def readCustomer(request,pk):
    customer = Customer.objects.get(pk=pk)
    orders = Order.objects.filter(customer=customer)
    return render(request, "templates/details.html", {'userId': pk, 'orders': orders, 'userName': customer.companyName})

def newOrder(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/orders/')
    else:
        form = OrderForm()

    fType = "order"

    return render(request, "templates/new-form.html", {'form':form,'formType':fType})
 
def newDriver(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/drivers/')
    else:
        form = DriverForm()

    fType = "driver"

    return render(request, "templates/new-form.html", {'form':form,'formType':fType})

def newCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/customers/')
    else:
        form = CustomerForm()

    fType = "customer"

    return render(request, "templates/new-form.html", {'form':form,'formType':fType})

def editDriver(request,pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == "POST":
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('/dash/drivers/')
    else:
        form = DriverForm(instance=driver)

    return render(request, "templates/new-form.html", {'form': form})

def editCustomer(request,pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/dash/customers/')
    else:
        form = CustomerForm(instance=customer)

    return render(request, "templates/new-form.html", {'form': form})
