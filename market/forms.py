from django import forms
from crispy_forms.helper import FormHelper
from .models import *

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

