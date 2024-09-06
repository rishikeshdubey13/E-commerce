from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.



#Create customer profile
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_mdodified = models.DateTimeField(auto_now =True)
    phone= models.CharField(max_length =20, blank =True)
    address1 = models.CharField(max_length =200, blank =True)
    address2= models.CharField(max_length =200, blank =True)
    city  = models.CharField(max_length =20, blank =True)
    state = models.CharField(max_length =20, blank =True)
    zipcode = models.CharField(max_length =20, blank =True)
    country = models.CharField(max_length =20, blank =True)

    def __str__(self):
        return self.user.username
    
# create  a profile for user when they register
def create_profile(sender,instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

#automate the Prfile creation
post_save.connect(create_profile,sender = User)



#category of prdocts
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    

 #customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=500)

    def __str__(self):
        return f' {self.first_name} {self.last_name}'


#all products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default = 1)
    description = models.CharField(max_length=1000,default = '',blank=True, null=True)
    image = models.ImageField(upload_to='upload/product/')
    is_sale = models.BooleanField(default = False)
    sale_price = models.DecimalField(default = 0 ,decimal_places= 2, max_digits=7)

    def __str__(self):
        return self.name



#customer orders
class Order(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantity  = models.IntegerField(default=1)
    # price = models.DecimalField()
    address = models.CharField(max_length =100)
    phone = models.CharField(max_length=11)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product



#Customer Wishlist
#class Wishlist(models.Model):
    


