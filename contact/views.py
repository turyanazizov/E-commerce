from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.contrib import messages

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your message has been received!')
            return redirect(reverse('contact:contact'))
            
    return render(request, 'contact.html', {'form': form})