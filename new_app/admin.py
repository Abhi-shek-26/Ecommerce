from django.contrib import admin
from django.contrib.auth.models import User

from new_app.models import Register, Seller, Buyer, Product, AddtoCart, BuyNow_tb

# Register your models here.

admin.site.register(Register)
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Product)
admin.site.register(AddtoCart)
admin.site.register(BuyNow_tb)
