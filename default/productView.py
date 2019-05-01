from django.shortcuts import render, redirect
from .productForm import AddProduct,ImportProduct
from .models import Product
from django.contrib import messages
from management.Constant import *

from django.core.files.storage import FileSystemStorage
import csv
import os
from django.conf import settings


def addProduct(request):
    if request.method == "POST":
        formData = AddProduct(request.POST)
        if formData.is_valid():
            formData.save()
            messages.success(request, success_saved)
            return redirect('/dashboard/product/add')
    else:
        form = AddProduct()
    return render(request, 'add_product.html', {'form': form})

def productList(request):
    recordList = Product.objects.order_by('id')
    return render(request, 'productlist.html', {'productList': recordList, 'flag':1})

def importProduct(request):
    if request.method == "POST" and request.FILES['import_product']:
        formFile = request.FILES['import_product']
        fs = FileSystemStorage()
        folder_path = settings.MEDIA_ROOT
        os.chdir(folder_path)
        file_extension = os.path.splitext(formFile.name)[1]
        if file_extension != '.csv':
            messages.error(request, file_type_error)
        else:
            fileName = fs.save(formFile.name, formFile)
            with open(fileName) as csvFile:
                reader = csv.DictReader(csvFile)
                for row in reader:
                    product = Product(title=row['title'],description=row['description'],
                    category_id=row['categories'],specification=row['specification'])
                    product.save()
                messages.success(request,import_message)
            os.remove(folder_path+ '/' + fileName)
            return redirect('/dashboard/category/list')
    form = ImportProduct()
    return render(request, 'importProduct.html', {'form':form})

def getProductByCat(request):
    productData=''
    cat_id = request.GET.get('categroy_id')
    if cat_id !='':
        productData = Product.objects.filter(category_id=cat_id)
    return render(request, 'product_option.html', {'data': productData})




    