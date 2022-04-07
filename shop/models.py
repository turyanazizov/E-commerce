from django.db import models
from multiselectfield import MultiSelectField


class Shops(models.Model):
    CATEGORIES = (
        ('1', 'Deactive'),
        ('2', 'Active'),
        ('3', 'Deactive'),
        ('4', 'Active'),
        ('5', 'Deactive'),
        ('6', 'Active'),
        ('7', 'Deactive'),
        ('8', 'Active'),
    )
    BRANDS = (
        ('1', 'Deactive'),
        ('2', 'Active'),
        ('3', 'Deactive'),
        ('4', 'Active'),
        ('5', 'Deactive'),
        ('6', 'Active'),
        ('7', 'Deactive'),
        ('8', 'Active'),
    )
    SIZES = (
        ('S', 'S'),
        ('XS', 'XS'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="shop/")
    price = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORIES)
    brand = models.CharField(max_length=50, choices=BRANDS)
    size = MultiSelectField(choices=SIZES)
        
        
    def __str__(self) :
        return self.title