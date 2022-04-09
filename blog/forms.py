from django.forms import ModelForm
from .models import Comments
from django import forms

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('name','phone','email','text','blog')

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "E-mail"}
            ),
            "text": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Comment"}
            ),
        }
