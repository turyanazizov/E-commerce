from django.shortcuts import render
from .models import About

def about(request):
    about=About.objects.all().first()
    context={
        'about':about,
    }
    return render(request,'about.html',context=context)
