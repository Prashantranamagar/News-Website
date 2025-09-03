from django.shortcuts import render, get_object_or_404, redirect
from .models import BlackList
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
import random
import string
import datetime

# Create your views here.


def black_list(request):

    ip = BlackList.objects.all()

    return render(request, 'back/blacklist.html', {'ip':ip})


def ip_add(request):

    if request.method == 'POST':

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        
        if len(str(day)) == 1 :
            day = "0" + str(day)
        if len(str(month)) == 1 :
            month = "0" + str(month)

    
        today = str(year) + "/" + str(month) + "/" + str(day)
        time = str(now.hour) + ":" + str(now.minute)


        ip = request.POST.get('ip')

        if ip != "" :

            b = BlackList(ip=ip, date=today)
            b.save()


    return redirect('black_list')


def ip_del(request,pk):
    
    b = BlackList.objects.filter(pk=pk)
    b.delete()

    return redirect('black_list')
