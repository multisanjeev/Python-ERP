from django.shortcuts import render,redirect
from django.contrib import messages
from .assetsForm import CreateOrder
from .models import Order,Stock
from employee.controlModel import Employee
from management.Constant import *
import datetime


def addAssets(request):
    if request.method == 'POST':
        formData = CreateOrder(request.POST)
        if formData.is_valid():
            current_stock = int(formData.cleaned_data['current_stock']) -1
            formData.save()
            Stock.objects.filter(pk=request.POST['product']).update(current_stock = current_stock)
            messages.success(request, success_saved)
        else:
            messages.error(request, form_error)
        return redirect('/dashboard/assest/list')
    else:
        form = CreateOrder()
    return render(request, 'createOrder.html', {'form': form})

def issueAssetsList(request):
    dataList = Order.objects.order_by('id')
    return render(request,'assetslist.html',{'assetsList': dataList,'flag':'1'})