from django.shortcuts import render , redirect

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def signup(request):
    return render(request,'pages/signup.html')

def login(request):
    return render(request , 'pages/login.html')

def logout(request):
    return redirect('index')
