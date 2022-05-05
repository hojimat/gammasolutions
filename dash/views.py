from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import RestrictedError
from .models import *
from .forms import OrderForm, DriverForm, CustomerForm
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
    customers = Customer.objects.all()
    return render(request, 'templates/customers.html', {'customers': customers})

def orders(request):
    orders = Order.objects.all()
    #orders = Order.objects.filter(deliveryDate__gt = ( datetime.today() - timedelta(days=30) ) )
    return render(request, 'templates/orders.html', {'orders': orders})

# READ MODELS

def readDriver(request,pk):
    driver = Driver.objects.get(pk=pk)
    orders = Order.objects.filter(driver=driver)
    return render(request, "templates/details.html", {'userId': pk, 'orders': orders, 'userName': f"{driver.firstName} {driver.lastName}"})

def readCustomer(request,pk):
    customer = Customer.objects.get(pk=pk)
    orders = Order.objects.filter(customer=customer)
    return render(request, "templates/details.html", {'userId': pk, 'orders': orders, 'userName': customer.companyName})

def readOrder(request,pk):
    order = Order.objects.get(pk=pk)
    return render(request, "templates/orderDetails.html", {'order': order})

# CREATE MODELS

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

# UPDATE MODELS

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

def editOrder(request,pk):
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

def deleteDriver(request,pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == "POST":
        try:
            driver.delete()
        except RestrictedError:
            pass

        return redirect('/dash/drivers/')
        
    return render(request, "templates/delete.html", {'userName': f"{driver.firstName} {driver.lastName}"})

def deleteCustomer(request,pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        try:
            customer.delete()
        except RestrictedError:
            pass

        return redirect('/dash/customers/')
        
    return render(request, "templates/delete.html", {'userName': customer.companyName})

def deleteOrder(request,pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        try:
            order.delete()
        except RestrictedError:
            pass

        return redirect('/dash/orders/')
        
    return render(request, "templates/delete.html", {'userName': f"Order #{pk}"})
