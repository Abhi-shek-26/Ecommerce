from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Register(AbstractUser):
    is_seller  = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)


class Seller(models.Model):
    reg_user = models.OneToOneField(Register, on_delete=models.CASCADE)

    seller_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)


class Buyer(models.Model):
    reg_user = models.OneToOneField(Register, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)


class Product(models.Model):

    category_choice =(
        ("Electronic","Electronic",),
        ("Clothing","Clothing",),
        ("Watches&Accesories","Watches&Accesories"),
        ("Books","Books"),
        ("Home&Lifestyles","Home&Lifestyles"),
        ("Food&Beverages","Food&Beverages"),
        ("Other","Other"),
    )

    Seller_data = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)

    productname = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    description = models.CharField(max_length=200)
    category = models.CharField(default="Electronic",choices=category_choice,max_length=30)
    count = models.IntegerField(default=1)
    image = models.FileField(upload_to='products/')


class AddtoCart(models.Model):
    reg_user = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    addproduct = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    status = models.BooleanField(default=False)

class BuyNow_tb(models.Model):
    reg_user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    quantity = models.IntegerField(default=1)

    status = models.BooleanField(default=False)


# class Order(models.Model):
#     reg_user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)




