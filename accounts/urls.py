from django.urls import path
from accounts.views import account

app_name = 'accounts'

urlpatterns = [
    path('', account, name='account'),
]