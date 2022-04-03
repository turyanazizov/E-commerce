from django.shortcuts import render
from . models import Blogs,Comments

def blog(request):
    blogs=Blogs.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request,'blog.html',context=context)

def blog_detail(request,id):
    blog = Blogs.objects.all().filter(id=id).first()
    comments = Blogs.objects.all().filter(id=id).first().comments.filter(status='Approve')
    context = {
        'blog': blog,
        'comments': comments
    }
    if request.method == "POST":
        Comments.objects.create(
            blog=Blogs.objects.all().filter(id=id).first(),
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            text=request.POST.get("text"),
        )
    return render(request,'blog-details.html',context=context)