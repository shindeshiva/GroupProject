from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
 



class project(models.Model):
    serialNo = models.TextField()
    country = models.TextField()
    isocode = models.TextField()
    year = models.TextField()
    total = models.TextField()
    coal = models.TextField()
    oil = models.TextField()
    gas = models.TextField()
    cement = models.TextField()
    flaring = models.TextField()
    other = models.TextField()

    def __str__(self):
        return self.serialNo, self.country, self.isocode, self.year, self.total, 
        self.coal, self.oil, self.gas, self.cement, self.flaring, self.other