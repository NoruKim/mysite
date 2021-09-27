from django.db import models

# Create your models here.


class Account(models.Model):
    email = models.TextField(primary_key=True)
    password = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    address_num = models.CharField(max_length=10)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'account'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        managed = False
        db_table = 'category'


class Products(models.Model):
    product_id = models.CharField(primary_key=True, max_length=5)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField(blank=True, null=True)
    product_desc = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    class Meta:
        managed = False
        db_table = 'products'