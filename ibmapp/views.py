from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse



# Create your views here.
def Registration(request):
    return render(request,'ibmapp/register.html')

def Login(request):
    return render(request,'ibmapp/login.html')

def register(request):
    print('inside register function')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    User( first_name =first_name, last_name = last_name, email = email, phone_number = phone, password = password ).save()

    data = User.objects.values_list('first_name')
    return render(request,'ibmapp/login.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    if User.objects.filter( email = email, password = password ):
       return render(request,'ibmapp/application.html')

def jsonDataResponse(request):
    data = list(User.objects.values())
    return JsonResponse(data, safe=False)

def application(request):
    return render(request,'ibmapp/application.html')

def apply(request):
    email = request.POST['email']
    experiance = request.POST['experiance']
    percentage_PG = request.POST['percentage_PG']
    percentage_UG = request.POST['percentage_UG']
    percentage_12th = request.POST['percentage_12th']
    percentage_10th = request.POST['percentage_10th']
    analytics_tools = request.POST.getlist('analytics_tools')
    SQL = request.POST.getlist('SQL')
    No_SQL = request.POST.getlist('No_SQL')
    Languages = request.POST.getlist('Languages')
    Big_Data_Ecosystem = request.POST.getlist('Big_Data_Ecosystem')
    
    data = {
        'email': email,
        'experience': experiance,
        'total_per_PG': percentage_PG,
        'total_per_G' : percentage_UG,
        'total_per_12' : percentage_12th,
        'total_per_10' : percentage_10th,
        'analytic_tools': analytics_tools,
        'languages' : Languages,
        'BDA_tools' : Big_Data_Ecosystem,
        'SQL_DB' : SQL,
        'NO_SQL_DB' : No_SQL
    }
    return JsonResponse( data, safe=False )
