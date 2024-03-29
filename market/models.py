from django.db import models
from datetime import date
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
        return f"{self.code} {self.core}, {self.state}"

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

class MarketCondition(models.Model):
    SUN = 'SUN'
    WND = 'WND'
    CLD = 'CLD'
    RNY = 'RNY'
    SNW = 'SNW'
    STM = 'STM'
    FOG = 'FOG'
    WEATHER = ((SUN, "Sunny"), (WND, "Windy"), (CLD, "Cloudy"), (RNY, "Rainy"), (SNW, "Snowy"), (STM, "Stormy"), (FOG, "Foggy"))

    city = models.ForeignKey(City, on_delete=models.RESTRICT, related_name="conditions", null=True, blank=True)
    date = models.DateField(blank=False, null=False, default=date.today)
    temperature = models.FloatField(default=0)
    precipitation = models.CharField(max_length=10, blank=True, choices=WEATHER, default=SUN)
    l2t_van = models.FloatField(blank=True, default=1.0) # loads to trucks ratio
    mci_van = models.FloatField(blank=True, default=1.0) # market conditions index by DAT
    rate_van = models.FloatField(blank=True, default=1.0) # average rate per mile
    l2t_reefer = models.FloatField(blank=True, default=1.0)
    mci_reefer = models.FloatField(blank=True, default=1.0)
    rate_reefer = models.FloatField(blank=True, default=1.0)

