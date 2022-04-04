from django.urls import path
from blog.views import blog,blog_detail

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('<slug:slug>', blog_detail, name='blog_detail'),
]