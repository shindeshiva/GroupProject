 from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
 



class countrydata(models.Model):
    serialNo = models.TextField(primary_key=True)
    country = models.TextField()
    isocode = models.TextField()
    year = models.TextField()

    def __str__(self):
        return f'{self.serialNo}, {self.country}, {self.isocode}, {self.year}'


class value(models.Model):
     serialNo = models.TextField(primary_key=True)
    total = models.ForeignKey('emissionapp.countrydata', on_delete=models.CASCADE, related_name='values')
    coal = models.TextField()
    oil = models.TextField()
    gas = models.TextField()
    cement = models.TextField()
    flaring = models.TextField()
    other = models.TextField()

    def __str__(self):
         return f'{self.serialNo}, {self.total}, {self.coal}, {self.oil}, {self.gas}
         {self.cement}, {self.flaring}, {self.other}'

        