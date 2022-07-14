from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=300)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    private_key=models.CharField(max_length=100)

class Admin(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=300)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    views=models.CharField(max_length=100)
    private_key=models.CharField(max_length=100)

class Product(models.Model):
    name=models.CharField(max_length=100)
    img=models.CharField(max_length=1000)
    desc=models.CharField(max_length=1000)
    price=models.CharField(max_length=100)
    tags=models.CharField(max_length=1000)
    quantity=models.CharField(max_length=100)
    features=models.CharField(max_length=1000)
    discount=models.CharField(max_length=100)
    category=models.CharField(max_length=1000)

class Category(models.Model):
    name=models.CharField(max_length=100)
    
class Cart(models.Model):
    productid=models.CharField(max_length=100)
    userid=models.CharField(max_length=100)

class Buy(models.Model):
    product_name=models.CharField(max_length=100)
    product_id=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    discount=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    user_id=models.CharField(max_length=100)
    
