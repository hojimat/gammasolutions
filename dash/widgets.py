from django import forms

class DateSelect(forms.DateInput):
    input_type = 'date'

class DateTimeSelect(forms.DateTimeInput):
    input_type = 'datetime'
