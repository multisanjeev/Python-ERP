from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from management.Constant import *
import datetime
from .stockForm import AddStock
from .models import Stock


def addStock(request):
    now = datetime.datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    if request.method == "POST":
        stockData = Stock.objects.filter(product_id=request.POST['product']).count()
        if stockData:
            check_stock = Stock.objects.get(product_id=request.POST['product'])
            current_stock = int(check_stock.current_stock) + int(request.POST['new_stock'])
            Stock.objects.filter(product_id = request.POST['product']).update(current_stock=current_stock,modified_at=today_date)
            messages.success(request, success_update)
        else:
            current_stock = int(request.POST['new_stock'])
            stock = Stock(product_id = request.POST['product'],current_stock=current_stock,new_stock=request.POST['new_stock'],
            created_at=today_date, modified_at=today_date)
            stock.save()
            messages.success(request, success_saved)
        return redirect('/dashboard/stock/list')
    else:
        form = AddStock()
    return render(request, 'add_stock.html', {'form': form})

def check_stock(request):
    product_id = request.GET.get('product_id')
    stock = list(Stock.objects.filter(product_id=product_id).values('current_stock'))
    data =  dict()
    if stock:
        data['stock'] = stock[0]['current_stock']
    else:
        data['stock'] = 0
    return JsonResponse(data)

def stockList(request):
    stockList = Stock.objects.all()
    return render(request, 'stocklist.html',{'stockList': stockList, 'flag': '1'})