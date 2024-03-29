from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import RestrictedError
from .models import *
from .forms import * 
from market.forms import CityForm
from datetime import datetime, timedelta
from django.contrib import messages

def index(request):
    return render(request, 'templates/index.html',)

def main(request):
    orders = Order.objects.select_related('origin_city','destination_city')
    earnings = orders.values('payment_due').annotate(gross=models.Sum('gross')).order_by('payment_due')
    earnings_by_driver = orders.values('driver').annotate(gross=models.Sum('gross')).values('driver__first_name','driver__last_name','gross')
    earnings_by_origin = orders.values('origin_city__metro_area__code').annotate(gross=models.Sum('gross'))
    earnings_by_destination = orders.values('destination_city__metro_area__code').annotate(gross=models.Sum('gross'))
    return render(request, 'templates/main.html', {'orders': orders,
                                                   'earnings': earnings,
                                                   'earnings_by_driver': earnings_by_driver,
                                                   'earnings_by_origin': earnings_by_origin,
                                                   'earnings_by_destination': earnings_by_destination,
                                                   })

# ALL MODELS

def drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'templates/drivers.html', {'drivers': drivers})

def customers(request):
    customers = Broker.objects.all()
    return render(request, 'templates/customers.html', {'customers': customers})

def orders(request):
    orders = Order.objects.select_related('origin_city','destination_city')
    return render(request, 'templates/orders.html', {'orders': orders})

def equipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'templates/equipment.html', {'equipment': equipment})

def documents(request):
    documents = Document.objects.all()
    return render(request, 'templates/documents.html', {'documents': documents})

def shippers(request):
    shippers = Shipper.objects.all()
    return render(request, 'templates/shippers.html', {'shippers': shippers})

# READ MODELS

def read_driver(request,pk):
    driver = Driver.objects.get(pk=pk)
    orders = driver.orders.select_related('origin_city','destination_city')
    earnings_wk = driver.earnings(days=7)
    earnings_yr = driver.earnings(days=365)
    earnings_hist = driver.earnings_history()
    documents = driver.documents.all()
    return render(request, "templates/entity-details.html", {'user': driver,
                                                             'userId': pk,
                                                             'orders': orders,
                                                             'earnings_wk': earnings_wk,
                                                             'earnings_yr': earnings_yr,
                                                             'earnings_hist': earnings_hist,
                                                             'documents': documents,
                                                             'whois': 'driver',
                                                             })

def read_customer(request,pk):
    customer = Broker.objects.get(pk=pk)
    orders = customer.orders.select_related('origin_city','destination_city')
    earnings_wk = customer.earnings(days=7)
    earnings_yr = customer.earnings(days=365)
    earnings_hist = customer.earnings_history()
    return render(request, "templates/entity-details.html", {'user': customer,
                                                             'userId': pk,
                                                             'orders': orders,
                                                             'earnings_wk': earnings_wk,
                                                             'earnings_yr': earnings_yr,
                                                             'earnings_hist': earnings_hist,
                                                             'whois': 'broker',
                                                             })

def read_order(request,pk):
    order = Order.objects.get(pk=pk)
    return render(request, "templates/order-details.html", {'order': order})

def read_shipper(request,pk):
    shipper = Shipper.objects.get(pk=pk)
    orders = shipper.orders.select_related('origin_city','destination_city')
    return render(request, "templates/entity-details.html", {'user': shipper,
                                                        'userId': pk,
                                                        'orders': orders,
                                                        'whois': 'shipper',
                                                        })


# CREATE MODELS

def new_order(request):
    city_form = None
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created an order.')
            return redirect('/dash/orders/')
    else:
        form = OrderForm()
        city_form = CityForm()

    return render(request, "templates/order-form.html", {'form':form, 'city_form':city_form})
 
def new_driver(request):
    if request.method == "POST":
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a driver.')
            return redirect('/dash/drivers/')
    else:
        form = DriverForm()

    return render(request, "templates/driver-form.html", {'form':form})

def new_customer(request):
    if request.method == "POST":
        form = BrokerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a customer.')
            return redirect('/dash/customers/')
    else:
        form = BrokerForm()

    return render(request, "templates/customer-form.html", {'form':form})

def new_equipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added an equipment.')
            return redirect(f"/dash/equipment/")
    else:
        form = EquipmentForm()

    return render(request, "templates/equipment-form.html", {'form':form})

def new_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a document.')
            return redirect(f"/dash/documents/")
    else:
        form = DocumentForm()

    return render(request, "templates/document-form.html", {'form':form})

def new_shipper(request):
    if request.method == "POST":
        form = ShipperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a shipper.')
            return redirect('/dash/shippers/')
    else:
        form = ShipperForm()

    return render(request, "templates/shipper-form.html", {'form':form})

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
    order = Order.objects.get(pk=pk)#select_related('driver').get(pk=pk)
    city_form = None
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the order information.')
            return redirect('/dash/orders/')
    else:
        form = OrderForm(instance=order)
        city_form = CityForm()

    return render(request, "templates/order-form.html", {'form': form, 'city_form': city_form})

def edit_equipment(request,pk):
    eqm = Equipment.objects.get(pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=eqm)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the equipment information.')
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
            messages.success(request, 'Successfully updated the document information.')
            return redirect('/dash/documents/')
    else:
        form = DocumentForm(instance=document)

    return render(request, "templates/document-form.html", {'form': form})

def edit_shipper(request,pk):
    shipper = Shipper.objects.get(pk=pk)
    if request.method == "POST":
        form = ShipperForm(request.POST, request.FILES, instance=shipper)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the shipper information.')
            return redirect('/dash/shippers/')
    else:
        form = ShipperForm(instance=shipper)

    return render(request, "templates/shipper-form.html", {'form': form})
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
    order = Order.objects.get(pk=pk)#select_related('driver').get(pk=pk)
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
            messages.warning(request, 'Successfully deleted the equipment.')
        except RestrictedError:
            pass

        return redirect('/dash/equipment/')
        
    return render(request, "templates/delete.html", {'object_name': eqm})


def delete_document(request,pk):
    document = Document.objects.get(pk=pk)
    if request.method == "POST":
        try:
            document.delete()
            messages.warning(request, 'Successfully deleted the document.')
        except RestrictedError:
            pass

        return redirect('/dash/documents/')
        
    return render(request, "templates/delete.html", {'object_name': document})

def delete_shipper(request,pk):
    shipper = Shipper.objects.get(pk=pk)
    if request.method == "POST":
        try:
            shipper.delete()
            messages.warning(request, 'Successfully deleted the shipper.')
        except RestrictedError:
            messages.error(request, 'Could not delete the shipper. Delete associated orders first.')
            pass

        return redirect('/dash/shippers/')
        
    return render(request, "templates/delete.html", {'object_name': shipper})
