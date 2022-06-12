from django.db import models
from dash.widgets import USCanadaStates

class Industry(models.Model):
    naics_code = models.IntegerField(blank=False, default=484)
    description = models.CharField(max_length=100, blank=False, default="Truck transportation")
    
    def __str__(self):
        return self.description

class Commodity(models.Model):
    sctg_code = models.IntegerField(blank=False, default=0)
    description = models.CharField(max_length=100, blank=False, default="SCTG suppressed")
    sctg_group = models.CharField(max_length=5, blank=False, default="0000")
    
    def __str__(self):
        return self.description

class MarketArea(models.Model):
    USA = 'USA'
    CND = 'CND'
    MEX = 'MEX'
    COUNTRIES = ( (USA, "USA"), (CND, "Canada"), (MEX, "Mexico") ) 

    center = models.CharField(max_length=30, blank=False, default="Chicago")
    state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default="IL")
    country = models.CharField(max_length=10, blank=False, choices=COUNTRIES, default=USA)

    def __str__(self):
        return f"{self.center}, {self.state}"

class StatArea(models.Model):
    csa_name = models.CharField(max_length=60, blank=False)
    state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default="IL")
    csa_code = models.IntegerField(blank=False, default=104) 
    state_code = models.IntegerField(blank=False, default=36)

    def __str__(self):
        return f"{self.csa_name}, {self.state}"

#class City(models.Model):
#    name = models.CharField(max_length=30, 

