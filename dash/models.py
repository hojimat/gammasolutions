from django.db import models
from .widgets import USCanadaStates
from datetime import datetime, timedelta

class Equipment(models.Model):
    FRM = 'FRM'
    OO = 'OO'
    OWNERS = ((FRM, "Company"), (OO, "Owner Operator"))

    RFR = 'RFR'
    VAN = 'VAN'
    FLT = 'FLT'
    TRK = 'TRK'
    TYPES = ((RFR, "Reefer"), (VAN, "Dry Van"), (FLT, "Flatbed"), (TRK, "Truck"), )

    owner = models.CharField(max_length=40, blank=False, default="Gamma Trucking LLC")
    ownership = models.CharField(max_length=10, blank=False, choices=OWNERS, default=OO)
    category = models.CharField(max_length=5, blank=False, choices=TYPES, default=VAN)
    vin = models.CharField(max_length=10, blank=True) # VIN number
    model = models.CharField(max_length=50, blank=False, default="")
    year = models.IntegerField(blank=True, default=2000)
    license_plate = models.CharField(max_length=10, blank=True)
    license_expiry = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, default=0) # max lbs
    width  = models.FloatField(blank=True, default=0) # ft
    height = models.FloatField(blank=True, default=0) # ft
    length = models.FloatField(blank=True, default=0) # ft
    active = models.BooleanField(default=True) # i.e. default truck/trailer at the moment

    def __str__(self):
        return f"{self.get_category_display()} {self.model} # {self.license_plate}"

#####################################################

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
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    class Meta:
        abstract = True

    def full_address(self):
        return f"{self.zip_code} {self.address}, {self.city}, {self.state}"
    
    def short_address(self):
        return f"{self.city}, {self.state}"

    def earnings(self, days=0):
        date_from = datetime.today() - timedelta(days=days) 
        all_earnings = self.orders.filter(payment_due__gt = date_from)
        total_earnings = all_earnings.aggregate(models.Sum('gross'))['gross__sum'] or 0.0
        return total_earnings

    def earnings_history(self):
        all_earnings = self.orders.values('payment_due').annotate(gross=models.Sum('gross')).order_by('payment_due')
        if not all_earnings.exists():
            return [{'payment_due': "Mar. 15, 2022", 'gross':100},
                    {'payment_due': "Jun. 15, 2022", 'gross':400}, 
                    {'payment_due': "Sep. 15, 2022", 'gross':500},
                    {'payment_due': "Dec. 15, 2022", 'gross':700}
                   ]
        return all_earnings
    
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

class Order(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT, related_name='orders', null=False)
    broker = models.ForeignKey(Broker, on_delete=models.RESTRICT, related_name='orders', null=True, blank=True)
    shipper = models.ForeignKey(Shipper, on_delete=models.RESTRICT, related_name='orders', null=True, blank=True)
    truck = models.ForeignKey(Equipment, on_delete=models.RESTRICT, related_name='truck_orders', null=True, blank=True)
    trailer = models.ForeignKey(Equipment, on_delete=models.RESTRICT, related_name='trailer_orders', null=True, blank=True)
    commodity = models.CharField(max_length=50, blank=True)
    origin_city = models.CharField(max_length=30, blank=False, default='New York')
    origin_state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default='NY')
    origin_address = models.CharField(max_length=70, blank=False, default='12 Broadway')
    origin_zip_code = models.CharField(max_length=10, blank=False, default='34342')
    origin_market = models.CharField(max_length=50, blank=True, default='')
    destination_city = models.CharField(max_length=30, blank=False, default='Palo Alto')
    destination_state = models.CharField(max_length=2, blank=False, choices=USCanadaStates, default='CA')
    destination_address = models.CharField(max_length=70, blank=False, default='1 Mountain View')
    destination_zip_code = models.CharField(max_length=10, blank=False, default='34341')
    destination_market = models.CharField(max_length=50, blank=True, default='')
    pickup_date = models.DateTimeField(blank=False, default="2022-01-13 08:00")
    delivery_date = models.DateTimeField(blank=False, default="2022-01-13 08:00")
    load_type = models.CharField(max_length=100, blank=False, default="palletized;lumper")
    temperature = models.FloatField(blank=True, default=70)
    instructions = models.CharField(max_length=500, blank=True)
    width  = models.FloatField(blank=True, default=0) # ft
    height = models.FloatField(blank=True, default=0) # ft
    length = models.FloatField(blank=True, default=0) # ft
    weight = models.FloatField(blank=True, default=0) # max lbs
    mileage = models.SmallIntegerField(blank=False, default=0)
    deadhead = models.SmallIntegerField(blank=False, default=0)
    gross = models.DecimalField(blank=False, max_digits=10, decimal_places=2, default=0)
    payment_due = models.DateField(blank=False, default="2022-01-13")
    g_rate = models.FloatField(blank=False, default=0) # to be inherited from Driver 
    fuel_burnt = models.FloatField(blank=False, default=0) # gallons
    fuel_price = models.DecimalField(blank=False, max_digits = 5, decimal_places=2, default=0) # USD per gallon
    toll = models.FloatField(blank=False, default=0)
    completed = models.BooleanField(default=False) 
    paid = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.pickup_date.strftime('%b %d')} {self.origin_state}-{self.destination_state} by {self.driver}"

    def origin_full_address(self):
        return f"{self.origin_zip_code} {self.origin_address}, {self.origin_city}, {self.origin_state}"

    def destination_full_address(self):
        return f"{self.destination_zip_code} {self.destination_address}, {self.destination_city}, {self.destination_state}"

    def origin_short_address(self):
        return f"{self.origin_city}, {self.origin_state}"

    def destination_short_address(self):
        return f"{self.destination_city}, {self.destination_state}"
    
    # def to return recent orders only (for last 30 days)
#####################################################

class Document(models.Model):
    CDL = 'CDL'
    DSP = 'DSP'
    MED = 'MED'
    DRG = 'DRG'
    BOL = 'BOL'
    INV = 'INV'
    RCON = 'RCON'
    STP = 'STP'
    DOCS = (
        (CDL, "Commercial Driver's License"),
        (DSP, "Dispatcher Agreement"),
        (MED, "Medical Card"),
        (DRG, "Drug Test"),
        (BOL, "Bill of Lading"),
        (INV, "Invoice"),
        (RCON, "Rate Confirmation"),
        (STP, "Setup document"),
    )
    name = models.CharField(max_length=10, blank=False, choices=DOCS, default=RCON)
    issue_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    issued_by = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=20, blank=True)
    detail = models.CharField(max_length=50, blank=True, default=0)
    scanned_copy = models.FileField(upload_to='documents/', blank=True, null=True) 
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT, related_name='documents', blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='documents', blank=True, null=True)
    broker = models.ForeignKey(Broker, on_delete=models.RESTRICT, related_name='documents', blank=True, null=True)
    
    def __str__(self):
        return self.name

#####################################################
