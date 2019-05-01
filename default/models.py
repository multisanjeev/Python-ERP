from django.db import models
from employee.controlModel import Employee

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255, null=True)
    display_order = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    description = models.CharField(max_length = 255)
    specification = models.TextField(null=True)

    def __str__(self):
        #return "%s is belong to %s" % (self.title, self.category)
        return "%s" % (self.title)

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    current_stock = models.IntegerField(default=0)
    new_stock = models.IntegerField(default=0)
    created_at = models.DateField()
    modified_at = models.DateField()

    def __str__(self):
        return "%s current stock = %s and new stock = %s" % (self.product,self.current_stock,self.new_stock)

class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    remark = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id
