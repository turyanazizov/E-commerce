from django.urls import path
from blog.views import BlogListView,blog_detail

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<slug:slug>', blog_detail, name='blog_detail'),
]