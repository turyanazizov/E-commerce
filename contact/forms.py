from django.forms import ModelForm
from . models import Contact
from django import forms

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name'
                }
            ),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            }),
        }