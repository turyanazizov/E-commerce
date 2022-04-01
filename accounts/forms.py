from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
User = get_user_model()

class RegistrationForm(UserCreationForm):

    password1 = forms.CharField(
        label=('Password'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new password', 'class': 'form-control', 'placeholder': 'New Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=('Confirm Password'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'Confirm password', 'class': 'form-control', 'placeholder': 'Confirm Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name',
            'email',
            'username',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        }