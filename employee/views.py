from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from employee.controlModel import Employee
from employee.loginForm import RegisterUserForm, LoginForm, AddEmployee,BulkImport
from management.Constant import *
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.core.files.storage import FileSystemStorage
import csv
import os
from django.conf import settings


#import pickle      
import json
#from django.core import serializers

# Create your views here.

def login(request):
    loginForm = LoginForm()
    val = [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
            ]
    if request.method == "POST":
        loginFormData = LoginForm(request.POST)
        if loginFormData.is_valid():
            data = ''
            try:
                employee_data = Employee.objects.get(email=loginFormData.cleaned_data['email'],password=loginFormData.cleaned_data['password'])
                data = {"full_name":employee_data.full_name,"email":employee_data.email,"contact":employee_data.contact}
                request.session['employee_data'] = data
                messages.success(request, login_success)
                return redirect('/dashboard')
            except Employee.DoesNotExist:
                messages.error(request, login_error)
    return render(request, "login.html", {'form': loginForm, 'value': val})

def register(request):
    if request.method == "POST":
        employeeData = RegisterUserForm(request.POST)
        if employeeData.is_valid():
            hasher = PBKDF2PasswordHasher()
            enc_password = hasher.encode(password=employeeData.cleaned_data['password'],salt='salt',iterations=50000)
            employeeData.cleaned_data['password'] = enc_password
            employeeData.save()
            messages.success(request, regiter_success)
            return redirect('/')
        else:
            messages.warning(request, regiter_error, extra_tags='alert-danger')
    else:
        registerForm = RegisterUserForm()
       
    return render(request, "register.html", {'form':registerForm})

def forgot(request):
    return render(request, 'forgot.html')

def logout(request):
    try:
        del request.session['employee_data']
        messages.success(request, 'Logout successfully.')
    except KeyError:
        pass
        messages.success(request, 'Logout successfully.')
    return redirect('/')

'''
Employee Management Area
'''

def addEmployee(request):
    if request.method == "POST":
        employeeData = AddEmployee(request.POST)
        if employeeData.is_valid():
            employeeData.save()
            messages.success(request, regiter_success)
        return redirect('/employee/list')
    else:
        employeeForm = AddEmployee()
    return render(request, 'add_employee.html',{'form': employeeForm})

def employe_list(request):
    data = Employee.objects.all()
    return render(request, 'employeeList.html',{'flag': '1', 'employeeList': data})

def bulkImportEmployee(request):
    if request.method == 'POST' and request.FILES['import_employee']:
        myfile = request.FILES['import_employee']
        fs = FileSystemStorage()
        file_extension = os.path.splitext(myfile.name)[1]
        if file_extension != '.csv':
            messages.error(request,file_type_error)
            return redirect('/employee/bulkImportEmployee')
        else:
            filename = fs.save(myfile.name, myfile)
            #uploaded_file_url = fs.url(filename)
            media_url = settings.MEDIA_ROOT # Set path of new directory here
            os.chdir(media_url) # changes the directory
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in  reader:
                    employee = Employee(full_name=row['full_name'],email=row['email'],contact=row['contact'],
                    password=row['password'])
                    employee.save()
                messages.success(request, import_message)
            os.remove(media_url+ '/' + filename)
            return redirect('/employee/list')
    else:
        bulkForm = BulkImport()
    return render(request, 'importEmployee.html', {'form': bulkForm})

