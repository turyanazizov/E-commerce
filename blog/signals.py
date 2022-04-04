from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.dispatch import receiver

from blog.models import Blogs
User = get_user_model()

@receiver(post_save, sender=Blogs)
def create_slug(instance, created, *args, **kwargs):
    if created:
        Blogs.objects.filter(id=instance.id).update(slug=slugify(instance.title))
