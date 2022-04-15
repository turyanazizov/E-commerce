from operator import truediv
from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse_lazy


class Categories(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brands(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Shops(models.Model):
    SIZES = (
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
        ("3XL", "3XL"),
    )
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="shop/")
    image2 = models.ImageField(upload_to="shop/",null=True,blank=True)
    image3 = models.ImageField(upload_to="shop/",null=True,blank=True)
    image4 = models.ImageField(upload_to="shop/",null=True,blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    size = MultiSelectField(choices=SIZES,null=True,blank=True)
    sale = models.BooleanField(default=False)
    brief_info = models.TextField(default='')
    description = models.TextField(default='')
    additional_information = models.TextField(default='')
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("shop:shop_detail", args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"
