from django import forms
from .models import *
from localflavor.us.forms import USStateSelect, USStateField

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'birthDate' : forms.DateInput(attrs={'type': 'date'}),
            'state' : USStateSelect(),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'state' : USStateSelect(),
        }

class DriverModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.firstName} {obj.lastName}"

class CustomerModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.companyName

class OrderForm(forms.ModelForm):
    driver = DriverModelChoiceField(queryset=Driver.objects.all(), empty_label="Choose")
    customer = CustomerModelChoiceField(queryset=Customer.objects.all(), empty_label="Choose")
    class Meta:
        model = Order
        exclude = ('gRate',)
        widgets = {
            'originState' : USStateSelect(),
            'destinationState' : USStateSelect(),
        }

