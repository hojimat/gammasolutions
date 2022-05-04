from django import forms

class DriverModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.firstName} {obj.lastName}"

class CustomerModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.companyName

class DateSelect(forms.DateInput):
    input_type = 'date'

class DateTimeSelect(forms.DateTimeInput):
    input_type = 'datetime'
