from django.db import models
from .widgets import USCanadaStates

class Entity(models.Model):
    phone = models.CharField(max_length=25, blank=True, default="+1(xxx)xxx-xx-xx")
    mobile = models.CharField(max_length=25, blank=True, default='+1(xxx)xxx-xx-xx')
    fax = models.CharField(max_length=25, blank=True, default='+1(xxx)xxx-xx-xx')
    telegram = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=False, default='example@example.com')
    zip_code = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=70, blank=True)
    city = models.CharField(max_length=30, blank=False, default='Palo Alto')
    state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default='CA')

    class Meta:
        abstract = True

    def full_address(self):
        return f"{self.zip_code} {self.address}, {self.city}, {self.state}"
    
    def short_address(self):
        return f"{self.city}, {self.state}"
    
class Driver(Entity):
    GENDERS = (('M',"Male"),('F',"Female"),('X',"Do not specify"))
    first_name = models.CharField(max_length=20, blank=False, default="Scott")
    last_name = models.CharField(max_length=20, blank=False, default="Pilgrim")
    birth_date = models.DateField(null=True, blank=True, default="1990-3-15")
    gender = models.CharField(max_length=10, choices=GENDERS, default='M')
    mc = models.CharField(max_length=10, blank=True) # MC number
    usdot = models.CharField(max_length=10, blank=True) # DOT number
    g_rate = models.FloatField(blank=False, default=0) # my percentage from gross
    active = models.BooleanField(default=True) # to filter out non-active drivers
    emergency_contact_name = models.CharField(max_length=40, blank=True, default="Young Neil")
    emergency_contact_phone = models.CharField(max_length=25, blank=True, default="+1(xxx)xxx-xx-xx")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#####################################################

class Customer(Entity):
    company_name = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    contact_name_1 = models.CharField(max_length=40, blank=False, default='Scott Pilgrim')
    contact_name_2 = models.CharField(max_length=40, blank=False, default='Ramona Flowers')

    class Meta:
        abstract = True

    def __str__(self):
        return self.company_name

class Broker(Customer):
    mc = models.CharField(max_length=10, blank=True)
    usdot = models.CharField(max_length=10, blank=True)

class Shipper(Customer):
    industry = models.CharField(max_length=20, blank=True)
    ein = models.CharField(max_length=20, blank=True) # IRS EIN number

#####################################################

class Equipment(models.Model):
    FRM = 'FRM'
    OO = 'OO'
    OWNERS = ((FRM, "Company"), (OO, "Owner Operator"))

    ownership = models.CharField(max_length=10, blank=False, choices=OWNERS, default=OO)
    vin = models.CharField(max_length=10, blank=True) # VIN number
    model = models.CharField(max_length=10, blank=True)
    year = models.IntegerField(blank=True)
    license_plate = models.CharField(max_length=10, blank=True)
    license_expiry = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True) # i.e. default truck/trailer at the moment

    class Meta:
        abstract = True

    def __str__(self):
        self.model

class Trailer(Equipment):
    RFR = 'RFR'
    VAN = 'VAN'
    FLT = 'FLT'
    TYPES = ((RFR, "Reefer"), (VAN, "Dry Van"), (FLT, "Flatbed"), )

    category = models.CharField(max_length=10, blank=False, choices=TYPES, default=VAN)
    driver = models.ManyToManyField(Driver, related_name='trailers')

    def __str__(self):
        self.category

class Truck(Equipment):
    driver = models.ManyToManyField(Driver, related_name='trucks')

#####################################################

class Order(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT, related_name='orders', null=False)
    broker = models.ForeignKey(Broker, on_delete=models.RESTRICT, related_name='orders', null=True, blank=True)
    shipper = models.ForeignKey(Shipper, on_delete=models.RESTRICT, related_name='orders', null=True, blank=True)
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)
    trailer = models.ForeignKey(Trailer, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)
    commodity = models.CharField(max_length=50, blank=True)
    origin_city = models.CharField(max_length=30, blank=False, default='New York')
    origin_state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default='NY')
    origin_address = models.CharField(max_length=70, blank=False, default='12 Broadway')
    origin_zip_code = models.CharField(max_length=10, blank=False, default='34342')
    origin_market = models.CharField(max_length=50, blank=False, default=0)
    destination_city = models.CharField(max_length=30, blank=False, default='Palo Alto')
    destination_state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default='CA')
    destination_address = models.CharField(max_length=70, blank=False, default='1 Mountain View')
    destination_zip_code = models.CharField(max_length=10, blank=False, default='34341')
    destination_market = models.CharField(max_length=50, blank=False, default=0)
    pickup_date = models.DateTimeField(blank=False, default="2022-01-13 08:00AM")
    delivery_date = models.DateTimeField(blank=False, default="2022-01-13 08:00AM")
    load_type = models.CharField(max_length=100, blank=False, default="palletized;lumper")
    temperature = models.FloatField(blank=True, default=70)
    instructions = models.CharField(max_length=500, blank=True)
    mileage = models.SmallIntegerField(blank=False, default=0)
    deadhead = models.SmallIntegerField(blank=False, default=0)
    gross = models.FloatField(blank=False, default=0)
    payment_due = models.DateField(blank=False, default="2022-01-13")
    g_rate = models.FloatField(blank=False, default=0) # to be inherited from Driver 
    fuel_burnt = models.FloatField(blank=False, default=0) # gallons
    fuel_price = models.FloatField(blank=False, default=0) # USD per gallon
    toll = models.FloatField(blank=False, default=0)

    def origin_full_address(self):
        return f"{self.origin_zip_code} {self.origin_address}, {self.origin_city}, {self.origin_state}"

    def destination_full_address(self):
        return f"{self.destination_zip_code} {self.destination_address}, {self.destination_city}, {self.destination_state}"

    def origin_short_address(self):
        return f"{self.origin_city}, {self.origin_state}"

    def destination_short_address(self):
        return f"{self.destination_city}, {self.destination_state}"

#####################################################

class Document(models.Model):
    name = models.CharField(max_length=50, blank=False, default=0)
    issue_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    issued_by = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=20, blank=True)
    detail = models.CharField(max_length=50, blank=True, default=0)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class DriverDocument(Document):
    CDL = 'CDL'
    DSP = 'DSP'
    MED = 'MED'
    DRG = 'DRG'
    DOCS = (
        (CDL, "Commercial Driver's License"),
        (DSP, "Dispatcher Agreement"),
        (MED, "Medical Card"),
        (DRG, "Drug Test"),
    )
    name = models.CharField(max_length=10, blank=False, choices=DOCS, default=CDL)
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT, related_name='documents', null=False)

class OrderDocument(Document):
    BOL = 'BOL'
    INV = 'INV'
    RCON = 'RCON'
    DOCS = (
        (BOL, "Bill of Lading"),
        (INV, "Invoice"),
        (RCON, "Rate Confirmation"),
    )
    name = models.CharField(max_length=10, blank=False, choices=DOCS, default=BOL)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='documents', null=False)

class BrokerDocument(Document):
    STP = 'STP'
    DOCS = (
        (STP, "Setup document"),
    )
    name = models.CharField(max_length=10, blank=False, choices=DOCS, default=STP)
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT, related_name='broker_dox', null=False)
    broker = models.ForeignKey(Broker, on_delete=models.RESTRICT, related_name='documents', null=False)

#####################################################
