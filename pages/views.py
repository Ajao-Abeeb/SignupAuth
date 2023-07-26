from django.shortcuts import render , redirect
from django.contrib import messages
# from django.contrib.auth import password_validation
from django.contrib.auth.models import User 
from django.contrib import auth


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def signup(request):
    if request.method == 'POST':
         username = request.POST['username']
         email = request.POST['email']
         check = request.POST['check']
         password = request.POST['password']
         con = request.POST['con']
         if password == con:
             if User.objects.filter(email = email).exists():
                 messages.error(request, 'Username already exists')
                 return redirect('signup')
             else:
                user= User.objects.create_user(username=username,email=email,password=password)
                auth.login(request , user)
                messages.success(request, 'You are now logged in')
                return redirect('index')
                user.save()
                messages.success(request, 'You register successfully')
                return redirect('login')
             
         else:
             messages.error(request, 'Password does not match')
             return redirect('signup')
    else:
      return render(request,'pages/signup.html')

def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = auth.authenticate(username=username,password=password)
         if user != None :
             auth.login(request , user)
             return redirect('index')
    return render(request , 'pages/login.html')

def logout(request):
    return redirect('index')

def PasswordResetConfirmView(request):
    
    return redirect(request , 'pages/password_reset_complete.html')