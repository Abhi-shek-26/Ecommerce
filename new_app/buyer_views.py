from django.contrib import messages
from django.shortcuts import redirect, render

from new_app.filters import ProductFilter
from new_app.forms import LoginForm, BuyerForm, BuyNowForm
from new_app.models import Buyer, Product, AddtoCart, BuyNow_tb


def Buyer_add(request):
    login_form = LoginForm()
    Buyer_form = BuyerForm()

    if request.method == 'POST':
        login_form2 = LoginForm(request.POST)
        Buyer_form1 =BuyerForm(request.POST)


        if login_form2.is_valid() and Buyer_form1.is_valid():
            log = login_form2.save(commit=False)
            log.is_buyer = True
            log.save()

            buyer_data = Buyer_form1.save(commit=False)
            buyer_data.reg_user = log
            buyer_data.save()
            return redirect('login_view')


    return render(request,'buyer/buyerReg.html',{'login_form':login_form,'Buyer_form':Buyer_form})



def buyer_viewbase(request):
    return render(request, 'Buyer/buyer_base.html')


def buyer_profile_view(request):
    user_data = request.user
    print(user_data.id)

    buyer_data = Buyer.objects.get(reg_user= user_data)

    return  render (request,"Buyer/buyer_profile.html",{"buyer_data":buyer_data})

def edit_buyer_profile(request):
    user_data = request.user
    buyer_data = Buyer.objects.get(reg_user = user_data)

    form = BuyerForm(instance = buyer_data)


    if request.method == 'POST':
        form = BuyerForm(request.POST,instance = buyer_data)
        if form.is_valid():
            form.save()
            return redirect('/buyer_profile_view/')
    return render(request,'buyer/buyer_edit_profile.html',{'form':form})


def buyer_view_productdetails(request):
    products = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)  # request.GET is key
    return render(request, 'Buyer/buyer_viewproduct.html', {
        'products': product_filter.qs,
        'product_filter': product_filter
    })


def addtocart(request,id):
    user_data = request.user
    buyer_data = Buyer.objects.get(reg_user=user_data)
    # print(buyer_data)

    product = Product.objects.get(id=id)
    # print(product)


    obj =AddtoCart()
    obj.reg_user = buyer_data
    obj.addproduct = product
    obj.save()

    # AddtoCart.objects.create(reg_user_id = buyer_data.id, addproduct_id = product.id)
    return redirect('buyer_view_productdetails')


def cart_view(request):
    data = AddtoCart.objects.all()
    return render(request, 'Buyer/cartview.html',{'data':data})


def delete_cart(request,id):
    data = AddtoCart.objects.get(id=id)
    data.delete()
    return redirect('cart_view')




def BuyNowCart(request, id):
    cart_item = AddtoCart.objects.get(id=id)
    product = cart_item.addproduct
    buyer = cart_item.reg_user

    if request.method == 'POST':
        form = BuyNowForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.reg_user = buyer
            obj.product = product

            if obj.quantity > product.count:
                messages.error(request, "Insufficient Quantity.")
                return redirect(request.path)   # stop here

            # Enough stock
            product.count -= obj.quantity
            product.save()
            obj.save()

            cart_item.delete()
            messages.success(request, "Order placed successfully.")
            return redirect('cart_view')

    else:
        form = BuyNowForm(initial={
            'email': buyer.email,
            'phone_number': buyer.phone_number,
            'address': buyer.address,
        })

    return render(request, 'Buyer/chekout.html', {
        'form': form,
        'cart': cart_item
    })




def BuyNowHome(request, id):
    product = Product.objects.get(id=id)
    buyer = Buyer.objects.get(reg_user=request.user)

    if request.method == 'POST':
        form = BuyNowForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.reg_user = buyer
            obj.product = product

            if obj.quantity > product.count:
                messages.error(request, "Insufficient Quantity.")
                return redirect(request.path)

            # Enough stock
            product.count -= obj.quantity
            product.save()
            obj.save()

            messages.success(request, "Order placed successfully.")
            return redirect('buyer_view_productdetails')

    else:
        form = BuyNowForm(initial={
            'email': buyer.email,
            'phone_number': buyer.phone_number,
            'address': buyer.address
        })

    return render(request, 'Buyer/chekout.html', {
        'form': form,
        'product': product
    })


def Orders(request):
    buyer = Buyer.objects.get(reg_user=request.user)

    orders = BuyNow_tb.objects.filter(
        reg_user=buyer
    ).order_by('-id')

    return render(request, 'Buyer/orders.html', {'orders': orders})

def delete_order(request, id):
    order = BuyNow_tb.objects.get(id=id)
    order.delete()
    return redirect('Orders')

def product_list(request):
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'Buyer/product_list.html', {'filter': filter})




