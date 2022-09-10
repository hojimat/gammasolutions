from django.test import TestCase
from .models import *
from market.models import *
from datetime import datetime, timezone
from .widgets import USCanadaStates
from decimal import Decimal

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name = "Ramona",
            last_name = "Flowers",
            birth_date = "1991-01-02",
            gender = "F",
            mc = "1234567",
            g_rate = 0.3,
            active = True)
        
        self.broker = Broker.objects.create(
            zip_code = "343434",
            address = "Sunset Bvd 32",
            city = "Arlington",
            state = "TX",
            mc = "7654321")

        self.commodity = Commodity.objects.create(
            sctg_code = 234,
            description = "Trucking",
            sctg_group = "234x")

        self.origin_city = City.objects.create(
            name = "Santa Fe",
            state = "NM",
            time_zone = 'MT'
        )
        self.destination_city = City.objects.create(
            name = "Palo Alto",
            state = "CA",
            time_zone = 'PT'
        )

        self.order = Order.objects.create(
            driver = self.driver,
            broker = self.broker,
            commodity = self.commodity,
            origin_city = self.origin_city,
            origin_address = "Brooklyn 99",
            origin_zip_code = "1299",
            destination_city = self.destination_city,
            pickup_date = datetime(2022,3,11,10,35,tzinfo=timezone.utc),
            delivery_date = datetime(2022,3,15,18,0,tzinfo=timezone.utc),
            load_type = "lumper",
            mileage = 689,
            deadhead = 45,
            gross = 1200.34,
            payment_due = datetime(2022,3,30,18,0),
            g_rate = 8.5,
            fuel_burnt = 50,
            fuel_price = 250,
            toll = 0.0
        )
    
    def test_driver(self):
        ''' Tests the Driver model '''
        self.assertEqual(str(self.driver), "Ramona Flowers")

    def test_order_driver(self):
        ''' Tests order-driver relation '''
        self.assertEqual(self.order.driver, self.driver)
        self.assertEqual(self.driver.orders.first(), self.order)

    def test_order_broker(self):
        ''' Tests order-broker relation '''
        self.assertEqual(self.order.broker, self.broker)
        self.assertEqual(self.broker.orders.first(), self.order)

    def test_full_address(self):
        self.assertEqual(self.order.broker.full_address(), f"343434 Sunset Bvd 32, Arlington, TX")

    def test_short_address(self):
        self.assertEqual(self.order.broker.short_address(), f"Arlington, TX")

    def test_earnings(self):
        self.assertEqual(self.driver.earnings(days=1000), Decimal('1200.34'))
