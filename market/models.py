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

    core = models.CharField(max_length=30, blank=False, default="Chicago")
    state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default="IL")
    country = models.CharField(max_length=10, blank=False, choices=COUNTRIES, default=USA)

    def __str__(self):
        return f"{self.core}, {self.state}"

    class Meta:
        ordering = ('state',)

class StatArea(models.Model):
    core = models.CharField(max_length=60, blank=False)
    state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default="IL")
    code = models.IntegerField(blank=False, default=104) 
    fips = models.IntegerField(blank=False, default=36)

    def __str__(self):
        return f"{self.core}, {self.state}"

    class Meta:
        ordering = ('state',)

class MetroArea(models.Model):
    core = models.CharField(max_length=60, blank=False)
    state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default="IL")
    code = models.IntegerField(blank=False, default=602) 
    fips = models.IntegerField(blank=False, default=36)

    def __str__(self):
        return f"{self.code}:{self.state}:{self.core}"

    class Meta:
        ordering = ('state',)
        
class City(models.Model):
    ET = 'ET'
    CT = 'CT'
    MT = 'MT'
    PT = 'PT'
    TIMEZONES = ( (ET, 'Eastern Time'), (CT, 'Central Time'), (MT, 'Mountain Time'), (PT, 'Pacific Time') )
    name = models.CharField(max_length=30, blank=False, default="Chicago")
    state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default="IL")
    market_area = models.ForeignKey(MarketArea, on_delete=models.RESTRICT, related_name="cities", null=True, blank=True)
    stat_area = models.ForeignKey(StatArea, on_delete=models.RESTRICT, related_name="cities", null=True, blank=True)
    metro_area = models.ForeignKey(MetroArea, on_delete=models.RESTRICT, related_name="cities", null=True, blank=True)
    time_zone = models.CharField(max_length=2, blank=False, choices=TIMEZONES, default=ET)

    def __str__(self):
        return f"{self.name}, {self.state}"

    class Meta:
        ordering = ('name','state')
        constraints = (models.UniqueConstraint(fields=('name','state'), name='unique_city'),)
