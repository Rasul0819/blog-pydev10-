from django.shortcuts import render,get_object_or_404
from . import models
# Create your views here.

def homepage(request):
    posts = models.BlogModel.objects.all()

    return render(request,'home.html',{'posts':posts})


def detail(request,id):
    post = get_object_or_404(models.BlogModel,id=id)
    return render(request,'detail.html',{'post':post})
