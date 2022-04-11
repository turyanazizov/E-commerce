from django.db import models
from django.urls import reverse_lazy

class Blogs(models.Model):
    published_date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogs/')
    # Blog Details fields
    content1 = models.TextField()
    content2 = models.TextField()
    quote = models.TextField()
    quote_owner =models.CharField(max_length=100)
    publisher_name=models.CharField(max_length=100)
    publisher_img = models.ImageField(upload_to='blogs/')
    tags=models.CharField(max_length=100,)
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
    text=models.TextField()
    name=models.CharField(max_length=100,)
    email=models.EmailField()
    phone=models.CharField(max_length=100,)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name