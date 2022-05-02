from django import forms
from .models import *

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
        fields = ('pickupDate', 'driver', 'customer',)
