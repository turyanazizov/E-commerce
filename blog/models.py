from asyncore import read
from faulthandler import disable
from tkinter import DISABLED
from django.db import models
from django.urls import reverse_lazy

class Blogs(models.Model):
    published_date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogs/', null=False, blank=False)
    # Single Blog fields
    content1 = models.TextField(blank=False,null=False)
    content2 = models.TextField(blank=False,null=False)
    quote = models.TextField(blank=False,null=False)
    quote_owner =models.CharField(max_length=100,blank=False,null=False)
    publisher_name=models.CharField(max_length=100,blank=False,null=False)
    publisher_img = models.ImageField(upload_to='blogs/', null=False, blank=False)
    tags=models.CharField(max_length=100,blank=False,null=False)
    slug=models.SlugField(max_length=255,blank=True,null=True)
    
    def get_absolute_url(self):
        return reverse_lazy('blog:blog_detail', args=[self.slug])
    

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return f"{self.publisher_name}'s Blog"

class Comments(models.Model):
    STATUS_CHOICES = (
        ('Approve', 'Approve'),
        ('Reject', 'Reject'),
    )
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE,blank=True,null=True,related_name='comments')
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)
    text=models.TextField(blank=False,null=False)
    name=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(blank=False,null=False)
    phone=models.CharField(max_length=100,blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name