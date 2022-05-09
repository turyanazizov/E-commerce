from django.forms import ModelForm
from django import forms

class ContactForm(forms.Form):

    full_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Full Name'}))    
    email = forms.EmailField(max_length = 150, widget=forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'E-mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Your message'}))

    def send_email(self):
        pass