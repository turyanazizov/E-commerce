from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(data=request.POST) # eger formda file varsa --> files=request.FILES
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
            # messages.success(f'{user.first_name}, welcome to our website!')
            # site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            # send_confirmation_email(user_id=user.id, site_address=site_address)
    context = {'form': form}
    return render(request, 'register.html',context)


def login(request):
    return render(request,'login.html')