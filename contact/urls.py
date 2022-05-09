from django.urls import path
from contact.views import ContacView
app_name = 'contact'

urlpatterns = [
    path('', ContacView.as_view(), name='contact'),
]