from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.dispatch import receiver
from shop.models import Shops

User = get_user_model()

@receiver(post_save, sender=Shops)
def create_slug(instance, created, *args, **kwargs):
    if created:
        Shops.objects.filter(id=instance.id).update(slug=slugify(instance.title))