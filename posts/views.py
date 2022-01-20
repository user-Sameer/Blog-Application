from django.shortcuts import render
from .models import posts

# Create your views here.

def index(request):

    post = posts.objects.all() ## gets the all objects in database

    context={
        'post': post
    }


    return render(request , 'index.html', context)


def post(request,pk):
    post=posts.objects.get(id=pk)

    context={
        'post':post
    }
    return render(request,'post.html', context)
