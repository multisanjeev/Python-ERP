"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views, productView, stockView, assetsView, reportView

app_name = 'datasheet'

urlpatterns = [
    path('', views.default, name="dashboard"),
    path('category/add', views.addCategory, name="addCategory"),
    path('category/list', views.categoryList, name="categoryList"),
    path('category/import', views.importCategory, name="import_category"),
    path('product/add', productView.addProduct, name="addProduct"),
    path('product/list', productView.productList, name="productList"),
    path('product/import', productView.importProduct, name="import_product"),
    path('product/getList', productView.getProductByCat, name="ajaxCall"),
    path('stock/add', stockView.addStock, name="addStock"),
    path('stock/check', stockView.check_stock, name="checkStock"),
    path('stock/list', stockView.stockList, name="stocklist"),
    path('assets/add', assetsView.addAssets, name="addAssests"),
    path('assest/list', assetsView.issueAssetsList, name="assetsList"),
    path('reports/employee', reportView.employeReport, name="employeeReport"),
    path('report/employeebyid/<int:employee>', reportView.employeeReportById, name="empReportById"),
    path('report/product', reportView.productReportDropDown, name="productDropDown")

]
