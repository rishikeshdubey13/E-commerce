from django.shortcuts import render, redirect
from .models import Product,Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, EditProfileForm
from django import forms

# Create your views here.



def category_summary(request):
    categories = Category.objects.all()
    return render(request,'category_summary.html', {"categories": categories})

def category(request,nm):
    #replace - with space
    nm = nm.replace('-',' ')
    try:
        category = Category.objects.get(name = nm)
        products =Product.objects.filter(category  = category)
        return render(request, 'category.html',{'category':category, 'products':products})
    except:
        messages.error(request,('This category does not exist'))
        return redirect('home')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html', {'product': product})

def home(request):
    products = Product.objects.all()
    return render(request,'home.html', {'products': products})

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,('You are logged in!'))
            return redirect('home')
        else:
            messages.success(request,('Error loggin in'))
            return redirect('login')
    else:   
        return render(request,'login.html')
        


def logout_user(request):
    logout(request)
    messages.success(request, ('You are logged out!'))
    return redirect('home')


def register(request):
    form =SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request, 'You have successfully registered')
            return redirect('login')
        else:
            messages.success(request, 'Error registering user')
            return redirect('register')
    else:   
        return render(request,'register.html', {'form': form})
    


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        user_form = EditProfileForm(request.POST or None, instance = current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request,('Your profile has been updated!'))
            return redirect('home') 
        return render(request,'update_user.html',{'user_form': user_form})
    else:
        messages.success(request,('login to access this page'))
        return redirect('update_user')
    
 
