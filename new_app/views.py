from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from new_app.forms import LoginForm, SellerForm, BuyerForm, ProductForm
from new_app.models import Register, Seller, Buyer, Product


# Create your views here.


def Login(request):
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_view_productdetails')
            elif user.is_seller:
                return redirect('view_product')
            elif user.is_buyer:
                return redirect('buyer_view_productdetails')
        else:
                print("Invalid credentials")

    return render(request,'login.html',{'login_form':login})


def landing_page(request):
    return render(request, 'index.html')

















