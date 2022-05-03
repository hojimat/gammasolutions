from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import OrderForm, DriverForm, CustomerForm

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

def newOrder(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            myOrder = form.save(commit=False)
            myOrder.gRate = myOrder.driver.gRate
            myOrder.save()
            
            return redirect('/dash/orders/')
    else:
        form = OrderForm()
        ftype = "order" 

    return render(request, "templates/new-form.html", {'form':form, 'formType':ftype})
 
def newDriver(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/drivers/')
    else:
        form = DriverForm()
        ftype = "driver" 

    return render(request, "templates/new-form.html", {'form':form, 'formType':ftype})

def newCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/customers/')
    else:
        form = CustomerForm()
        ftype = "customer" 

    return render(request, "templates/new-form.html", {'form':form, 'formType':ftype})
