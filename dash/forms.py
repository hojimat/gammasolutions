from django import forms
from localflavor.us.forms import USStateSelect, USStateField
from crispy_forms.helper import FormHelper
from .models import *
from .widgets import *

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'birthDate' : DateSelect(),
            'state' : USStateSelect(),
        }
        labels = {
            'firstName' : 'First name',
            'lastName' : 'Last name',
            'birthDate' : 'Birth date',
            'mc' : 'MC number',
            'usdot' : 'US DOT number',
            'cdl' : 'CDL',
            'vin' : 'VIN number',
            'zipCode' : 'ZIP code',
            'gRate' : 'Rate',
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'state' : USStateSelect(),
        }
        labels = {
            'companyName' : 'Company name',
            'firstName' : 'First name',
            'lastName' : 'Last name',
            'mc' : 'MC number',
            'usdot' : 'US DOT number',
            'zipCode' : 'ZIP code',
        }

class OrderForm(forms.ModelForm):
    driver = DriverModelChoiceField(queryset=Driver.objects.all(), empty_label="Choose")
    customer = CustomerModelChoiceField(queryset=Customer.objects.all(), empty_label="Choose")
    class Meta:
        model = Order
        exclude = ('gRate',)
        widgets = {
            'originState' : USStateSelect(),
            'destinationState' : USStateSelect(),
            'pickupDate' : DateTimeSelect(),
            'deliveryDate' : DateTimeSelect(),
        }
        labels = {
            'originCity' : 'PU city',
            'originState' : 'PU state',
            'originAddress' : 'PU address',
            'originZipCode' : 'PU ZIP code',
            'originMarket' : 'PU KMA',
            'pickupDate' : 'PU time',
            'destinationCity' : 'DO city',
            'destinationState' : 'DO state',
            'destinationAddress' : 'DO address',
            'destinationZipCode' : 'DO ZIP code',
            'destinationMarket' : 'DO KMA',
            'deliveryDate' : 'DO time',

        }

