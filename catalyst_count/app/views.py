from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from .models import *
import os
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
import threading
from django.contrib.auth import logout

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            #nikhil admin777
            user = authenticate(request,username = request.POST['email'],password = request.POST['password'])    
            if user is not None:
                auth_login(request, user)
                print('successfull')
                return redirect('/home')
            else:
                print('failed')
    return render(request,'login.html')

def clean_plus(num):
    return int(num.replace('+',''))

def insert_records(filename):
    chunksize = 50
    for df in pd.read_csv(filename, 
                            chunksize=5000):
        # df = pd.read_csv(filename)
        # df['size range'] = df['size range'].apply(clean_plus)
        df['year founded'] = df['year founded'].fillna(0)
        def city_split(st,mode):
            if ',' in str(st):
                if mode == 'city':
                    return st.split(',')[0].strip()
                else:
                    return st.split(',')[1].strip()
            else:
                return st

        records = [Upload(
            name = d['name'],
            domain = d['domain'],
            year_founded = d['year founded'],
            industry = d['industry'],
            size_range = d['size range'],
            city = city_split(d['locality'],'city'),
            state = city_split(d['locality'],'state'),
            country = d['country'],
            linkedin_url = d['linkedin url'],
            current_employee_estimate = d['current employee estimate'],
            total_employee_estimate = d['total employee estimate'],
            ) for d in df.to_dict(orient='records')]
        Upload.objects.bulk_create(records)
        print('Record insered-------------')

def home(request):
    if request.user.is_authenticated:
        if is_ajax(request):
            f = request.FILES['image']
            if f.name.split('.')[-1] == 'csv':
                filename = os.path.join('media','csv',str(f))
                with open(filename, "wb+") as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                insert_thread = threading.Thread(target=insert_records, name="Inserter", args=(filename,))
                insert_thread.start()
                insert_thread.join()
                # insert_records(df)
                return JsonResponse({'msg':'Upload completed'})
            else:
                return JsonResponse({'msg':'upload CSV file'})
        return render(request,'home.html')
    else:
        return redirect('/')
    
def view_user(request):
    if request.user.is_authenticated:
        all_users = User.objects.all()
        return render(request,'users.html',{'all_users':all_users})
    else:
        return redirect('/')
    
def query_builder(request):
    if request.user.is_authenticated:
        context = {
        'industry' : Upload.objects.order_by().values_list('industry', flat=True).distinct(),
        'year_founded' : Upload.objects.order_by().values_list('year_founded', flat=True).distinct(),
        'city' : Upload.objects.order_by().values_list('city', flat=True).distinct(),
        'state' : Upload.objects.order_by().values_list('state', flat=True).distinct(),
        'country' : Upload.objects.order_by().values_list('country', flat=True).distinct(),
        'current_employee_estimate' : [100,1000,10000,50000,100000],
        'total_employee_estimate' : [100,1000,10000,50000,100000]
        }
        return render(request,'query_builder.html',context)
    else:
        return redirect('/')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')

@csrf_protect 
@api_view(['POST'])
def query_output(request):
    context = {}
    if request.method == 'POST':
        query = {}
        if request.data.get('keyword',''):
            query['name'] = request.data.get('keyword','')

        if request.data.get('industry',''):
            query['industry'] = request.data.get('industry','')

        if request.data.get('city',''):
            query['city'] = request.data.get('city','')

        if request.data.get('state',''):
            query['state'] = request.data.get('state','')

        if request.data.get('country',''):
            query['country'] = request.data.get('country','')

        if request.data.get('emp_from',''):
            query['current_employee_estimate__gt'] = request.data.get('emp_from','')
        
        if request.data.get('emp_to',''):
            query['current_employee_estimate__lt'] = request.data.get('emp_to','')
        print(query)
        context['count'] = Upload.objects.filter(**query).count()
    return Response(context)

