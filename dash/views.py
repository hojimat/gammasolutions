from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

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

def brokers(request):
    brokers = Customer.objects.filter(entity="broker")
    return render(request, 'templates/customers.html', {'customers': brokers})

def shippers(request):
    shippers = Customer.objects.filter(entity="shipper")
    return render(request, 'templates/customers.html', {'customers': shippers})

def orders(request):
    orders = Order.objects.all()
    userName = "all users"
    if request.method == "POST":
        userType = request.POST.get("userType")
        userName = request.POST.get("userName")
        if userType=="driver":
            driver = request.POST.get("driverId")
            orders = Order.objects.filter(driver=driver)
        elif userType=="customer":
            customer = request.POST.get("customerId")
            orders = Order.objects.filter(customer=customer)
    return render(request, 'templates/orders.html', {'orders': orders, 'userName': userName})
