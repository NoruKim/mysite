from django.shortcuts import render , get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Products, Account
from .forms import ProductForm, AccountForm, SignupForm
# Create your views here.


def main(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        member = Account.objects.get(email=email, password=password)
        if member is not None:
            request.session['memberid'] = member.email
            products = Products.objects.order_by('product_id')
            return render(request, 'coupang/products_list.html', {'products': products, 'lName': member.last_name,
                                                                  'fName': member.first_name})
        else:
            return redirect('login')

    return render(request, 'coupang/products_list.html')


def login(request):
    form = AccountForm()
    return render(request, 'coupang/login.html', {'form': form})


def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'coupang/signup.html', {'form': form})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ProductForm()
    return render(request, 'coupang/product_create.html', {'form': form})


def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)

    return render(request, 'coupang/product_detail.html', {'product': product})


def product_update(request, pk):
    product = get_object_or_404(Products, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = ProductForm(instance=product)
    return render(request, 'coupang/product_update.html', {'form': form})


def product_delete(request, pk):
    product = Products.objects.get(pk=pk)
    product.delete()
    return redirect('main')