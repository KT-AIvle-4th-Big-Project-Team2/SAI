from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
#from .models import User form을 거치지 않고 
from .forms import signinForm
from .models import *

# Create your views here.
def testing(request):
    return HttpResponse("account app is running fine!")

def signIn(request):
    
    print(request.method)
    print("get: ", request.GET)
    print("get: ", request.POST)
    
    if request.method == 'POST':
        form = signinForm(request.POST)
        if form.is_valid():
            print("input valid")
            form.save()
            return redirect('new_account_success/')
        else:
            print("input not valid")

    return render(request, "account/signin.html")

def login(request):
    
    print(request.method)
    print("get: ", request.GET)
    print("get: ", request.POST)
    
    if request.method == 'POST':
        if User.objects.filter(name = request.POST.get('name')).exists():
            print("Matching username found!")
            potentialUser = User.objects.filter(name = request.POST.get('name')).first()
            if potentialUser.password == request.POST.get('password'):
                print("Password's also matchs!")
                return HttpResponse("Login successful!")
            else:
                return HttpResponse("Password is wrong! Your device will detonate in 10 seconds!")
        else:
            if Admin.objects.filter(name = request.POST.get('name')).exists():
                print("Matching admin name found!")
                
                potentialUser = Admin.objects.filter(name = request.POST.get('name')).first()
                if potentialUser.password == request.POST.get('password'):
                    print("Admin password's also matchs!")
                    return HttpResponse("Admin login successful!")
                else:
                    return HttpResponse("Password is wrong!\n Your device will detonate in 10 seconds!")
            else:
                return HttpResponse("Wrong ID!")
            

    return render(request, "account/login.html")

def signinSuccess(request):
    
    return HttpResponse("sign in successful!")