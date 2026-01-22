from django.contrib.auth.forms import UserCreationForm
from django import forms

from new_app.models import Register, Seller, Buyer, Product, BuyNow_tb


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ('username', 'password1', 'password2')


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields ='__all__'
        exclude = ('reg_user',)


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields ='__all__'
        exclude = ('reg_user',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('Seller_data',)


class BuyNowForm(forms.ModelForm):
    class Meta:
        model = BuyNow_tb
        fields = '__all__'
        exclude = ('reg_user',
                   'product',)
