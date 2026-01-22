from django.shortcuts import redirect, render

from new_app.forms import LoginForm, SellerForm, ProductForm
from new_app.models import Seller, Product


def Seller_add(request):
    login_form = LoginForm()
    Seller_form = SellerForm()

    if request.method == 'POST':
        login_form1 = LoginForm(request.POST)
        Seller_form1 = SellerForm(request.POST)

        if login_form1.is_valid() and Seller_form1.is_valid():
            log = login_form1.save(commit=False)
            log.is_seller = True
            log.save()

            seller_data = Seller_form1.save(commit=False)
            seller_data.reg_user = log
            seller_data.save()
            return redirect('login_view')

    return render(request, 'seller/sellerReg.html',{'login_form':login_form,'Seller_form':Seller_form})

def seller_viewbase(request):
    return render(request, 'Seller/seller_base.html')


def seller_profile_view(request):
    user_data = request.user
    print(user_data.id)

    seller_data = Seller.objects.get(reg_user= user_data)

    return render (request,"Seller/seller_profile.html",{"seller_data":seller_data})



def edit_seller_profile(request):

    user_data = request.user
    seller_data = Seller.objects.get(reg_user= user_data)


    form = SellerForm(instance=seller_data)

    if request.method == 'POST':
        form = SellerForm(request.POST,instance=seller_data)
        if form.is_valid():
            form.save()
            return redirect('/seller_profile_view/')
    return render(request,'seller/seller_edit_profile.html',{'form':form})


def add_product(request):
    user_data = request.user
    seller_data = Seller.objects.get(reg_user= user_data)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.Seller_data = seller_data
            data.save()
            return redirect('add_product')
    else:
        form = ProductForm()

    return render(request, 'Seller/add_product.html', {'ProductForm': form})

def view_product(request):
    user_data = request.user
    seller_data = Seller.objects.get(reg_user= user_data)
    product = Product.objects.filter(Seller_data = seller_data)
    return render(request, 'Seller/view_product.html', {'products': product})




def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('view_product')


def edit_product(request,id):
    product = Product.objects.get(id=id)

    form  = ProductForm(instance=product)

    if request.method ==  'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            data = form.save()
            return redirect('view_product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'Seller/edit_product.html', {'ProductForm': form})



