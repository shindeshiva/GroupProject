
from django.test import TestCase
from .models import countrydata, value

class countrydataTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up fake data only for the purpose of testing - not added to the real database
        cls.countrydata = countrydata.objects.create(
            serialNo='1',
            country='USA',
            isocode='US',
            year='1995'
        )
        cls.countrydata2 = countrydata.objects.create(
            serialNo='2',
            country='China',
            isocode='CN',
            year='2017'
        )

    def test_countrydata(self):
        self.assertEqual(str(self.countrydata), "USA")

    def test_countrydata_as_string(self):
        # we check if the returned string would match the expected one
        country = countrydata.objects.get(serialNo='2')
        expected_string = '2, country=China, isocode=CN, year=2017'
        self.assertEqual(str(country), expected_string)


class valueTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.country = countrydata.objects.create(
            serialNo='1',
            country='USA',
            isocode='US',
            year='1995'
        )
        cls.value = value.objects.create(
            serialNo='1',
            total=cls.country,
            coal='1000',
            oil='2000',
            gas='3000',
            cement='4000',
            flaring='5000',
            other='6000'
        )

    def test_value(self):
        self.assertEqual(str(self.value.oil), "2000")

    def test_value_as_string(self):
        val = value.objects.get(serialNo='1')
        expected_string = '1, total=1, coal=1000, oil=2000, gas=3000, cement=4000, flaring=5000, other=6000'
        self.assertEqual(str(val), expected_string)
        
"""
Running tests:

$ ./manage.py test

SOURCE: https://docs.djangoproject.com/en/4.1/topics/testing/overview/

"""
