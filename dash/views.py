from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import RestrictedError
from .models import *
from .forms import * 
from datetime import datetime, timedelta
from django.contrib import messages

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
    return render(request, 'templates/orders.html', {'orders': orders})

def equipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'templates/equipment.html', {'equipment': equipment})

def documents(request):
    documents = Document.objects.all()
    return render(request, 'templates/documents.html', {'documents': documents})

# READ MODELS

def read_driver(request,pk):
    driver = Driver.objects.get(pk=pk)
    orders = driver.orders.all()
    earnings = driver.earnings(days=300)
    documents = driver.documents.all()
    return render(request, "templates/driver-details.html", {'user': driver,
                                                             'userId': pk,
                                                             'orders': orders,
                                                             'earnings': earnings,
                                                             'documents': documents,
                                                             })

def read_customer(request,pk):
    customer = Broker.objects.get(pk=pk)
    orders = customer.orders.all()
    earnings = customer.earnings(days=300)
    return render(request, "templates/customer-details.html", {'user': customer,
                                                               'userId': pk,
                                                               'orders': orders,
                                                               'earnings': earnings,
                                                               })

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

    return render(request, "templates/order-form.html", {'form':form})
 
def new_driver(request):
    if request.method == "POST":
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dash/drivers/')
    else:
        form = DriverForm()

    return render(request, "templates/driver-form.html", {'form':form})

def new_customer(request):
    if request.method == "POST":
        form = BrokerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dash/customers/')
    else:
        form = BrokerForm()

    return render(request, "templates/customer-form.html", {'form':form})

def new_equipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/dash/equipment/")
    else:
        form = EquipmentForm()

    return render(request, "templates/equipment-form.html", {'form':form})

def new_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/dash/documents/")
    else:
        form = DocumentForm()

    return render(request, "templates/document-form.html", {'form':form})

# UPDATE MODELS

def edit_driver(request,pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == "POST":
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the driver information.')
            return redirect('/dash/drivers/')
    else:
        form = DriverForm(instance=driver)

    return render(request, "templates/driver-form.html", {'form': form})

def edit_customer(request,pk):
    customer = Broker.objects.get(pk=pk)
    if request.method == "POST":
        form = BrokerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the broker information.')
            return redirect('/dash/customers/')
    else:
        form = BrokerForm(instance=customer)

    return render(request, "templates/customer-form.html", {'form': form})

def edit_order(request,pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the order information.')
            return redirect('/dash/orders/')
    else:
        form = OrderForm(instance=order)

    return render(request, "templates/order-form.html", {'form': form})

def edit_equipment(request,pk):
    eqm = Equipment.objects.get(pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=eqm)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the order information.')
            return redirect('/dash/equipment/')
    else:
        form = EquipmentForm(instance=eqm)

    return render(request, "templates/equipment-form.html", {'form': form})

def edit_document(request,pk):
    document = Document.objects.get(pk=pk)
    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the order information.')
            return redirect('/dash/documents/')
    else:
        form = DocumentForm(instance=document)

    return render(request, "templates/document-form.html", {'form': form})

# DELETE MODELS

def delete_driver(request,pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == "POST":
        try:
            driver.delete()
            messages.warning(request, 'Successfully deleted the driver.')
        except RestrictedError:
            messages.error(request, 'Could not delete the driver. Delete associated orders first.')
            pass

        return redirect('/dash/drivers/')
        
    return render(request, "templates/delete.html", {'object_name': driver})

def delete_customer(request,pk):
    customer = Broker.objects.get(pk=pk)
    if request.method == "POST":
        try:
            customer.delete()
            messages.warning(request, 'Successfully deleted the customer.')
        except RestrictedError:
            messages.error(request, 'Could not delete the customer. Delete associated orders first.')
            pass

        return redirect('/dash/customers/')
        
    return render(request, "templates/delete.html", {'object_name': customer})

def delete_order(request,pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        try:
            order.delete()
            messages.warning(request, 'Successfully deleted the order.')
        except RestrictedError:
            pass

        return redirect('/dash/orders/')
        
    return render(request, "templates/delete.html", {'object_name': f"Order #{pk}"})

def delete_equipment(request,pk):
    eqm = Equipment.objects.get(pk=pk)
    if request.method == "POST":
        try:
            eqm.delete()
            messages.warning(request, 'Successfully deleted the order.')
        except RestrictedError:
            pass

        return redirect('/dash/equipment/')
        
    return render(request, "templates/delete.html", {'object_name': eqm})


def delete_document(request,pk):
    document = Document.objects.get(pk=pk)
    if request.method == "POST":
        try:
            document.delete()
            messages.warning(request, 'Successfully deleted the order.')
        except RestrictedError:
            pass

        return redirect('/dash/documents/')
        
    return render(request, "templates/delete.html", {'object_name': document})
