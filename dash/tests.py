from django.test import TestCase
from .models import *

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
    
    def test_driver(self):
        ''' Testing the Driver model '''
        ramona = Driver.objects.get(pk=self.driver.pk)
        self.assertEqual(str(ramona), "Ramona Flowers")
