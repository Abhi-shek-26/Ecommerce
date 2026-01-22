from django.shortcuts import render, redirect

from new_app.models import Seller, Buyer, Product


def admin_viewbase(request):
    return render(request, 'Admin/admin_base.html')


def view_seller(request):
    sellers = Seller.objects.select_related('reg_user').all()
    return render(request, 'Admin/view_seller.html', {'sellers': sellers})


def view_buyer(request):
    buyers = Buyer.objects.select_related('reg_user').all()
    return render(request, 'Admin/view_buyer.html', {'buyers': buyers})

def delete_seller(request,id):
    seller = Seller.objects.get(id=id)
    seller.delete()
    return redirect('/view_seller/')

def delete_buyer(request,id):
    buyer = Buyer.objects.get(id=id)
    buyer.delete()
    return redirect('/view_buyer/')


def admin_view_productdetails(request):
    products = Product.objects.all()
    return render(request, 'Admin/admin_viewproduct.html', {'products': products})