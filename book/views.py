from django.shortcuts import render,redirect
from django.db.models import Q
from.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.
def home(request):
    book = Book.objects.all()
    if request.method =='POST':
        search = request.POST.get('search')
        results = Book.objects.filter(Q(name__icontains=search) | Q(author__icontains=search))

        context = {
            'result':results
        }
        return render(request,'home.html',context)

    context = {
        'book':book,
    }
    return render(request,'home.html',context)

def login(request):
    if request.method=="POST":
        user = auth.authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html'),{'error': 'Username or password is incorrect'}
    else:
        return render(request,'login.html')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try :
                user = User.objects.get(username = request.POST['username'])
                return render(request,'signup.html',{"username already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                auth.login(request,user)
                return redirect('home')

    return render(request,'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def thankyou(request):
    if request.method == 'GET':
        return render(request,'thankyou.html')
    else:
        return redirect('home')