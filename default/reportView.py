from django.shortcuts import render,redirect
from .models import Product, Stock,Order
from employee.controlModel import Employee
from django.db.models import Count,Sum

def employeeReportById(request, employee):
    if employee:
        assetsList = Order.objects.filter(employee_id = employee).order_by('id')
    return render(request, 'employee_data.html', {'assetsList': assetsList, 'flag':1})

def employeReport(request):
    lists = Order.objects.values('employee_id', 'employee__full_name').annotate(num_qty = Sum("qty"))\
    .filter(num_qty__gt = 0).order_by('-num_qty')
    return render(request, 'employeeReport.html',{'lists': lists,'flag': '1'})

def productReportDropDown(request):
    dataList = Product.objects.order_by('title')
    return render(request, 'productDropDownForm.html', {'productList': dataList})

'''
def getStockDataById(request):
    prodId = request.GET.get('product_id')
    if prodId:
        productStockList = Stock.objects.filter(product_id = prodId).order_by('id')
    return render(request, 'productReportList', {'stockList': productStockList})
'''