from django.db import models

class Driver(models.Model):
    firstName = models.CharField(max_length=20, blank=False, default="Scott")
    lastName = models.CharField(max_length=20, blank=False, default="Pilgrim")
    birthDate = models.DateField(null=True, blank=True, default="1990-3-15")
    phone = models.CharField(max_length=25, blank=True, default="+1")
    telegram = models.CharField(max_length=20, blank=True)
    mc = models.CharField(max_length=10, blank=True) # MC number
    usdot = models.CharField(max_length=10, blank=True) # DOT number
    cdl = models.CharField(max_length=10, blank=True) # CDL number
    vin = models.CharField(max_length=10, blank=True) # VIN number
    trailer = models.CharField(max_length=10, blank=True) # Trailer number
    address = models.CharField(max_length=70, blank=True)
    zipCode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=False, default='Palo Alto')
    state = models.CharField(max_length=2, blank=False, default='CA')
    gRate = models.FloatField(blank=False, default=0) # my percentage from gross

class Customer(models.Model):
    firstName = models.CharField(max_length=20, blank=False, default='Scott')
    lastName = models.CharField(max_length=20, blank=False, default='Pilgrim')
    phone = models.CharField(max_length=25, blank=True, default='1(xxx)xxx-xx-xx')
    telegram = models.CharField(max_length=20, blank=True)
    mc = models.CharField(max_length=10, blank=True)
    usdot = models.CharField(max_length=10, blank=True)
    companyName = models.CharField(max_length=50, blank=True)
    entity = models.CharField(max_length=20, blank=True) # broker or shipper or else?
    address = models.CharField(max_length=70, blank=True)
    zipCode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=False, default='New York')
    state = models.CharField(max_length=2, blank=False, default='NY')

class Order(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT, related_name='orders', null=False)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='orders', null=False)
    originCity = models.CharField(max_length=30, blank=False, default='New York')
    originState = models.CharField(max_length=2, blank=False, default='NY')
    originAddress = models.CharField(max_length=70, blank=False, default=0)
    originZipCode = models.CharField(max_length=10, blank=True)
    originMarket = models.CharField(max_length=50, blank=False, default=0)
    destinationCity = models.CharField(max_length=30, blank=False, default='Palo Alto')
    destinationState = models.CharField(max_length=2, blank=False, default='CA')
    destinationAddress = models.CharField(max_length=70, blank=False, default=0)
    destinationZipCode = models.CharField(max_length=10, blank=True)
    destinationMarket = models.CharField(max_length=50, blank=False, default=0)
    pickupDate = models.DateTimeField(blank=False, default="2022-01-13 08:00AM")
    deliveryDate = models.DateTimeField(blank=False, default="2022-01-13 08:00AM")
    mileage = models.SmallIntegerField(blank=False, default=0)
    deadhead = models.SmallIntegerField(blank=False, default=0)
    gross = models.FloatField(blank=False, default=0)
    paymentDue = models.DateField(blank=False, default="2022-01-13")
    gRate = models.FloatField(blank=False, default=0) # to be inherited from Driver 
    fuelBurnt = models.FloatField(blank=False, default=0) # gallons
    fuelPrice = models.FloatField(blank=False, default=0) # USD per gallon
    toll = models.FloatField(blank=False, default=0)


class Document(models.Model):
    issueDate = models.DateTimeField()
    expiryDate = models.DateTimeField()
    entity = models.CharField(max_length=50, blank=False, default=0)
    result = models.CharField(max_length=50, blank=False, default=0)


#class Truck:
#    pass
# one-to-one relation with Driver
# color, year, make, model etc;
