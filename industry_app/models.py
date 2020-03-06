from django.db import models

# Create your models here.
class Devices(models.Model):
    type = models.CharField(max_length=100,blank=False)
    price = models.IntegerField()

    choises = (('AVAILABLE','Available to Purchase'),('SOLD','Item Sold'),('OUT OF STOCK','Restoring Soon'))
    status = models.CharField(max_length=20,default='SOLD',choices=choises)
    issues = models.CharField(max_length=100,default='NO ISSUES')

    class Meta:
        abstract = True

    def __str__(self):
        return 'type : {0} price : {1}'.format(self.type,self.price)

class Laptop(Devices):
    pass

class Mobile(Devices):
    pass

class Desktop(Devices):
    pass
