from django.db import models

class About(models.Model):
    image = models.ImageField(upload_to='about/')
    title1 = models.CharField(max_length=100)
    content1 = models.TextField()
    title2 = models.CharField(max_length=100)
    content2 = models.TextField()
    title3 = models.CharField(max_length=100)
    content3 = models.TextField()
    
    def __str__(self):
        return 'About Model'