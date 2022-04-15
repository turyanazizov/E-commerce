from django.shortcuts import render
from blog.models import Blogs

def index(request):
    some_blogs=Blogs.objects.all()[0:3]
    context={
        'some_blogs':some_blogs,
    }
    return render(request,'index.html',context=context)
