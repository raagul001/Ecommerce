from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def filename(request,filename):
    time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(time,filename)
    return os.path.join('uploads/',new_filename)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to=filename, null=True, blank=True)
    Description = models.TextField(max_length=700, null=False, blank=False)
    Status = models.BooleanField(default=False, help_text="0-show, 1-hidden")
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name


class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    Vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=filename, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    Description = models.TextField(max_length=700, null=False, blank=False)
    Status = models.BooleanField(default=False, help_text="0-show, 1-hidden")
    Trending = models.BooleanField(default=False, help_text="0-default, 1-trending")
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)

  @property
  def total_cost(self):
    return self.product_qty*self.product.selling_price
  
class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)