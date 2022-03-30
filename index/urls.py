from django.urls import path
from index.views import index

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
]