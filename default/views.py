from django.shortcuts import render,redirect
from django.contrib import messages
from management.Constant import *
from django.core.files.storage import FileSystemStorage
import csv
import os
from django.conf import settings
from .forms import CategoryForm, ImportCategory
from .models import Categories

# Create your views here.

def default(request):
    if 'employee_data' not in request.session:
        return redirect ('/')
    return render(request, 'dashboard.html')

def addCategory(request):
    if 'employee_data' not in request.session:
        return redirect ('/')
    if request.method == "POST":
        formData = CategoryForm(request.POST)
        if formData.is_valid():
            print(formData.cleaned_data)
            formData.save()
            messages.success(request,success_saved)
        return redirect('/dashboard/category/list')
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'form': form})

def categoryList(request):
    if 'employee_data' not in request.session:
        return redirect ('/')
    categoryList = Categories.objects.order_by('id')
    return render(request, 'categorylist.html', {'categoryList': categoryList, 'flag':1})

def importCategory(request):
    if 'employee_data' not in request.session:
        return redirect ('/')
    if request.method == "POST" and request.FILES['import_category']:
        uploadedFile = request.FILES['import_category']
        fs = FileSystemStorage()
        file_extension = os.path.splitext(uploadedFile.name)[1]
        if file_extension != '.csv':
            messages.error(request,file_type_error)
        else:
            fileName = fs.save(uploadedFile.name, uploadedFile)
            folder_path = settings.MEDIA_ROOT
            os.chdir(folder_path)
            with open(fileName) as csvFile:
                reader = csv.DictReader(csvFile)
                for row in reader:
                    category = Categories(title=row['title'],description=row['description'],display_order=row['display_order'])
                    category.save()
                messages.success(request, import_message)
            os.remove(folder_path+ '/' + fileName)
            return redirect('/dashboard/category/list')
    else:
        form = ImportCategory()
    return render(request, 'importCategory.html', {'form': form})
    
