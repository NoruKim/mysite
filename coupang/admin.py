from django.contrib import admin
from . models import Account, Category, Products
# Register your models here.

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Products)