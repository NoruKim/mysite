from django import forms
from .models import Products, Account


class ProductForm(forms.ModelForm):

    class Meta:

        model = Products
        fields = ['product_id', 'product_name', 'product_price', 'product_desc', 'category']


class AccountForm(forms.ModelForm):

    class Meta:

        model = Account
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'email'}),
            'password': forms.PasswordInput,
        }


class SignupForm(forms.ModelForm):
    password_check = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'pw2'}))

    class Meta:

        model = Account
        fields = ['email', 'password', 'password_check', 'last_name', 'first_name', 'address_num', 'address1',
                  'address2', 'phone']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'pw1'}),
        }