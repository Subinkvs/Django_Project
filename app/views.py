from django.shortcuts import render, redirect
from .forms import CustomUserCreation
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('home.html')
    else:
        form =CustomUserCreation()
    context = {
        'form':form
    }       
    return render(request, 'signup.html', context)
        
def login_view(request):
    if request.method == 'POST':
        form = CustomUserCreation(data= request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home.html')
        else:
            form = CustomUserCreation(data=request.POST)
    context = {
        'form':form
    } 
    return render(request, 'login.html', context)
 
@login_required       
def logout_view(request):
    logout(request)
    return redirect('login.html')
        
        
        
    
