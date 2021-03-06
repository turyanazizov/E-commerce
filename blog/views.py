from re import template
from django.shortcuts import get_object_or_404, render
from . models import Blogs
from .forms import CommentsForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView,DetailView

class BlogListView(ListView):
    template_name = 'blog.html'
    model = Blogs
    paginate_by = 3
    context_object_name = 'blogs'

def blog_detail(request,slug):
    blog = get_object_or_404(Blogs, slug=slug)
    comments = Blogs.objects.all().filter(slug=slug).first().comments.filter(status='Approve')
    form = CommentsForm()
    if request.method == "POST":
        blog_field=Blogs.objects.all().filter(slug=slug).first()
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.blog=blog_field
            form.save()
            messages.info(request, 'Your comment has been sended!')
            return redirect('blog:blog_detail' , slug=blog.slug)
    context = {
        'blog': blog,
        'comments': comments,
        'form':form,
    }
    return render(request,'blog-details.html',context=context)
