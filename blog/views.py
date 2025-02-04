from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login, authenticate,logout
from .forms import RegisterForm,LoginForm,BlogForm
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request):
    posts = models.BlogModel.objects.all()

    return render(request,'home.html',{'posts':posts})


def detail(request,id):
    post = get_object_or_404(models.BlogModel,id=id)
    return render(request,'detail.html',{'post':post})

def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():#duris toltirilganba?
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})


def login_view(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(form.cleaned_data)
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required#logindi soraw
def create_post(request):
    if request.method =='POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request,'create_post.html',{'form':form}) 


