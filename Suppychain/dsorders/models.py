from ast import Pass
from curses.ascii import NUL
import email
from email.headerregistry import Address
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver 
from decimal import Decimal
from django.core.validators import MinValueValidator
# Create your models here.

class User(AbstractUser):
    pass

class Dealer(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name',null=True,blank=True)
    phone = models.CharField(max_length=15,verbose_name='Phone Number',unique=True)
    persons_name = models.CharField(max_length=100,verbose_name="Person's name",null=True,blank=True)
    additional_info = models.CharField(max_length=100,null=True,blank=True)
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="dealer_user")
    
    def __str__(self):
        return self.name
   
    class Meta:
        verbose_name_plural = 'Dealer'
        
class Salesman(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name',null=True,blank=True)
    phone = models.CharField(max_length=12,verbose_name='Phone number',unique=True)
    address = models.CharField(max_length=50,verbose_name='Address',null=True,blank=True)
    additional_info = models.TextField(max_length=100,null=True,blank=True)
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL,related_name='Salesman_user')
    dealer = models.ForeignKey(Dealer,on_delete=models.SET_NULL,related_name='dealer',null=True,blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Salesman'

class Item(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name',null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=0,validators=[MinValueValidator(Decimal('0.01'))],verbose_name='Price',null=True,blank=True)
    selling_unit = models.CharField(max_length=100)
    description = models.TextField(max_length=500,verbose_name='Description',null=True,blank=True)
    dealer = models.ForeignKey(Dealer,on_delete=models.SET_NULL,null=True,blank=True,related_name='Dealer1')
   
    class Meta:
        verbose_name_plural = 'Item'
        
    def __str__(self):
        return self.name

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date Ordered')
    salesman = models.ForeignKey(Salesman,on_delete=models.CASCADE,related_name='salesman_orders',verbose_name='Salesman')

    class Meta:
        verbose_name_plural ='Order'
    
    
    
class Shop(models.Model):
    name = models.CharField(max_length=100,verbose_name='Shop name')
    address = models.CharField(max_length=100,null=True,blank=True,verbose_name='Address')
    phone = models.CharField(max_length=16,null=True,blank=True)
    additional_info = models.TextField(max_length=100,null=True,blank=True)
    dealer = models.ForeignKey(Dealer,on_delete=models.SET_NULL,related_name='Shop_salesman',verbose_name='Salesman',null=True,blank=True)

    def __str__(self):
        return self.name

class orderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.CharField(max_length=100,null=True,blank=True,default="")

    class Meta:
        verbose_name_plural ='Order Item'

@receiver(pre_save,sender=Dealer)
def create_user_for_dealer(sender,instance,**kwargs):
    try:
       user = User.objects.get(username=instance.phone)
    except User.DoesNotExist:
        User.objects.create_user(username=instance.phone,email="",password=instance.phone)


@receiver(pre_save,sender=Salesman)
def create_user_for_salesman(sender,instance,**kwargs):
    try:
       user = User.objects.get(username=instance.phone)
    except User.DoesNotExist:
        User.objects.create_user(username=instance.phone,email="",password=instance.phone)

@receiver(post_save,sender=Dealer)
def linking_dealer(sender,instance,**kwargs):
    user = User.objects.get(username=instance.phone)
    if instance.user is None:
        instance.user = user
        instance.save()

@receiver(post_save,sender=Salesman)
def linking_salesman(sender,instance,**kwargs):
    user = User.objects.get(username=instance.phone)
    if instance.user is None:
        instance.user = user
        instance.save()

