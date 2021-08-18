from django.db import models
from homeapp.models import *

# Create your models here.
class cartlist(models.Model):
    cart_id = models.CharField(max_length=250,unique=True)
    dateadded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    prdct = models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quant = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prdct

    def total(self):
        return self.prdct.price*self.quant