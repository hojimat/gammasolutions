from django.test import TestCase
from .models import *
from datetime import datetime, timezone
#from .widgets import USCanadaStates
from decimal import Decimal

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        self.commodity = Commodity.objects.create(
            sctg_code = 234,
            description = "Trucking",
            sctg_group = "234x")

        self.city = City.objects.create(
            name = "Palo Alto",
            state = "CA",
            time_zone = 'PT'
        )
    
    def test_city(self):
        ''' Tests the city string '''
        self.assertEqual(str(self.city), "Palo Alto, CA")

    def test_commodity(self):
        ''' Tests the commodity string '''
        self.assertEqual(str(self.commodity), "Trucking")

