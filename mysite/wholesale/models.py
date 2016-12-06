from django.db import models


class Product(models.Model):
    Name = models.CharField('Product Name', max_length=20)
    Price = models.DecimalField('Product Price', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.Name


class Customer(models.Model):
    Firstname = models.CharField('Customer Firstname', max_length=20)
    Lastname = models.CharField('Customer Lastname', max_length=20)
    Location = models.CharField('Customer Location', max_length=20)

    def __str__(self):
        return self.Firstname


class Order(models.Model):
    Pid = models.ForeignKey(Product, on_delete=models.CASCADE)
    Cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Qty = models.IntegerField()

    def __str__(self):
        return self.Cid.Firstname


