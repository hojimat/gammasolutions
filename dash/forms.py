from django import forms
from crispy_forms.helper import FormHelper
from .models import *
from .widgets import *

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'birth_date' : DateSelect(),
        }
        labels = {
            'mc' : 'MC number',
            'usdot' : 'US DOT number',
            'g_rate' : 'Default charge rate',
        }

class BrokerForm(forms.ModelForm):
    class Meta:
        model = Broker
        fields = '__all__'
        labels = {
            'mc' : 'MC number',
            'usdot' : 'US DOT number',
        }

class OrderForm(forms.ModelForm):
    driver = forms.ModelChoiceField(queryset=Driver.objects.all(), empty_label="Choose")
    broker = forms.ModelChoiceField(queryset=Broker.objects.all(), empty_label="Choose")
    shipper = forms.ModelChoiceField(queryset=Shipper.objects.all(), empty_label="Choose", required=False)
    #equipment = forms.ModelChoiceField(queryset=Equipment.objects.all(), empty_label="Choose", required=False)
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'pickup_date' : DateTimeSelect(),
            'delivery_date' : DateTimeSelect(),
            'payment_due' : DateSelect(),
        }
        labels = {
            'destination_zip_code' : 'Destination ZIP',
            'origin_zip_code' : 'Origin ZIP',
            'g_rate' : 'Default charge rate',
        }

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        labels = {
            'vin': 'VIN number',
            'weight': 'Max load capacity (lbs)',
            'height': 'Height (ft)',
            'width': 'Width (ft)',
            'length': 'Length (ft)',
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        widgets = {
            'issue_date': DateSelect(),
            'expiry_date': DateSelect(),
        }
