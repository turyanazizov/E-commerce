from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView

class ContacView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')
    def form_valid(self, form):
        messages.info(self.request, 'Your message has been received!')
        return super().form_valid(form)