from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.views.generic import FormView

# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Your message has been received!')
#             return redirect(reverse('contact:contact'))
            
#     return render(request, 'contact.html', {'form': form})

class ContacView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)